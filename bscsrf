
url="<put your url here>"
cookies=()

IFS=$'\r
' GLOBIGNORE='*' command eval 'cookies+=($(curl -s -i -X GET $url | grep -i set-cookie))'
for cookie in "${cookies[@]}"; do
  cookie=$(echo "$cookie" | sed 's/.*: //')
  cookies+=( $(echo "$cookie" | cut -f1 -d';') )
done

data=\"<put your POST data here>"
data+="&csrf_token=fake_token"
curl -s -i -b "$(printf "%s;" "${cookies[@]}" | sed 's/;*$//')" -X POST -d "$data" -H "Content-Type: application/x-www-form-urlencoded" --max-time 20 -o /dev/null -w "%{http_code}" $url > response.txt

if grep -q "403" response.txt; then
  echo "The URL $url has CSRF protection enabled."
elif grep -q "200" response.txt; then
  echo "The URL $url does not have CSRF protection enabled."
else
  echo "An error occurred."
fi

rm response.txt
