function docker-taglist {
  if [ ! -z $1 ]; then
    curl -s https://registry.hub.docker.com/v1/repositories/$1/tags | sed "s/,/\n/g" | grep name | cut -d '"' -f 4
    # curl -s https://hub.docker.com/v2/repositories/$1/tags/list | jq
  else
    echo -e "\nusage: docker-taglist [imagename]\n"
  fi
}

function docker-container-ip {
  if [ ! -z $1 ]; then
    if [ ! -z $2 ]; then
      NET_NAME="\"$2\""
    else
      NET_NAME="bridge"
    fi
    docker inspect $1 | jq -r ".[0].NetworkSettings.Networks.${NET_NAME}.IPAddress"
  else
    echo -e "\nusage: docker-container-ip [container-name] [container-network]\n"
  fi
}

function docker-taglist2 () { 
    local repo=${1} 
    local page_size=${2:-100} 
    [ -z "${repo}" ] && echo "Usage: listTags <repoName> [page_size]" 1>&2 && return 1 
    local base_url="https://registry.hub.docker.com/api/content/v1/repositories/public/library/${repo}/tags" 
     
    local page=1 
    local res=$(curl "${base_url}?page_size=${page_size}&page=${page}" 2>/dev/null) 
    local tags=$(echo ${res} | jq --raw-output '.results[].name') 
    local all_tags="${tags}" 
 
    local tag_count=$(echo ${res} | jq '.count')   
 
    ((page_count=(${tag_count}+${page_size}-1)/${page_size}))  # ceil(tag_count / page_size) 
 
    for page in $(seq 2 $page_count); do 
        tags=$(curl "${base_url}?page_size=${page_size}&page=${page}" 2>/dev/null | jq --raw-output '.results[].name') 
        all_tags="${all_tags}${tags}" 
    done 
 
    echo "${all_tags}" | sort 
} 
