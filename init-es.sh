curl -XDELETE "http://localhost:9200/monte-iato"
echo
curl -XPUT "http://localhost:9200/monte-iato"
echo
curl -XPUT "http://localhost:9200/monte-iato/unit/_mapping" -d @mapping.json
echo
