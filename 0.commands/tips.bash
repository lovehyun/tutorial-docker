function docker-taglist {
  if [ ! -z $1 ]; then
    curl -s https://registry.hub.docker.com/v1/repositories/$1/tags | sed "s/,/\n/g" | grep name | cut -d '"' -f 4
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
