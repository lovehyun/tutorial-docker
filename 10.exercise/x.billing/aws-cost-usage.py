#!/usr/bin/env python3

import argparse
import boto3
import datetime


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--days', type=int, default=90)
    parser.add_argument('--profile', type=str, default="default")
    parser.add_argument('--resolution', type=str, default="MONTHLY")
    args = parser.parse_args()

    return args


def process_dates(args):
    now = datetime.datetime.utcnow()
    if args.resolution == 'MONTHLY':
        start = (now - datetime.timedelta(days=args.days)).strftime('%Y-%m-01')
    else:
        start = (now - datetime.timedelta(days=args.days)).strftime('%Y-%m-%d')
    end = now.strftime('%Y-%m-%d')

    return start, end


def retrieve_from_aws(args, start, end):
    session = boto3.session.Session(profile_name=args.profile)
    ce_client = session.client('ce', 'us-east-1')

    results = []
    token = None

    while True:
        if token:
            kwargs = {'NextPageToken': token}
        else:
            kwargs = {}

        data = ce_client.get_cost_and_usage(
            TimePeriod = {'Start': start, 'End': end}, 
            Granularity = args.resolution, 
            Metrics = ['UnblendedCost'], 
            GroupBy = [{'Type': 'DIMENSION', 'Key': 'LINKED_ACCOUNT'}, {'Type': 'DIMENSION', 'Key': 'SERVICE'}], 
            **kwargs)

        results += data['ResultsByTime']
        token = data.get('NextPageToken')
        if not token:
            break

    return results


def parse_results(results):
    print('\t'.join(['TimePeriod', 'Amount', 'Unit', 'Est.', 'LinkedAccount', 'Service']))
    for result_by_time in results:
        sum = 0
        for group in result_by_time['Groups']:
            amount = float(group['Metrics']['UnblendedCost']['Amount'])
            unit = group['Metrics']['UnblendedCost']['Unit']
            services = '\t'.join(group['Keys'])

            print("{}\t{:7.2f}\t{}\t{}\t{}".format(
                result_by_time['TimePeriod']['Start'], 
                amount, 
                unit, 
                result_by_time['Estimated'], 
                services))
            sum += amount
        print('TOTAL:\t{:7.2f}'.format(sum))
        print('-'*20)


def main():
    args = parse_arguments()
    start, end = process_dates(args)
    results = retrieve_from_aws(args, start, end)
    parse_results(results)


if __name__ == "__main__":
    main()
