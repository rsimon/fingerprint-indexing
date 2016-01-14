curl -XGET "http://localhost:9200/monte-iato/_search?pretty" -d '{
  "query": {
    "nested" : {
      "path": "fingerprint_ceramic",
      "query": {
        "fuzzy": {
          "fingerprint_ceramic.kurzzeit_lagerung_transport.imitat_hybrid": {
            "value": 2,
            "fuzziness": 1
          }
        }
      }
    }
  }
}'
echo
