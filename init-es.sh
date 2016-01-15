curl -XDELETE "http://localhost:9200/monte-iato"
echo
curl -XPUT "http://localhost:9200/monte-iato"
echo
curl -XPUT "http://localhost:9200/monte-iato/assemblage/_mapping" -d @mapping_new.json
echo
