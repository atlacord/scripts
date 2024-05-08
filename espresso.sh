# A script to launch our Minecraft server. Also updates Paper to the latest build for the MC version the server uses.

#!/bin/bash
api=https://papermc.io/api/v2
name=paper
version=1.20.4
memory=8G

# Get the build number of the most recent build
latest_build="$(curl -sX GET "$api"/projects/"$name"/versions/"$version"/builds -H 'accept: application/json' | jq '.builds [-1].build')"

# Construct download URL
download_url="$api"/projects/"$name"/versions/"$version"/builds/"$latest_build"/downloads/"$name"-"$version"-"$latest_build".jar

rm paper.jar

# Download file
wget "$download_url"
echo "Updating  Paper to version "$version" "$latest_build""

mv "$name"-"$version"-"$latest_build".jar paper.jar
echo "Successfully updated Paper! Starting server."

# Start server instance
java -Xms"$memory" -Xmx"$memory" -jar paper.jar --nogui
