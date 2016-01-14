for filename in `ls data/*`; do
  curl -XPOST "http://localhost:9200/monte-iato/unit" -d @$filename
  echo
done
