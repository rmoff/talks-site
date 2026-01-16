---
title: "🚢 All at Sea with Streams - Using Kafka to Detect Patterns  in the Behaviour of Ships"
slug: "all-at-sea-with-streams-using-kafka-to-detect-patterns-in-the-behaviour-of-ships-qrgjuz"
date: 2021-09-14T08:00:00
event: "Kafka Summit Americas"
location: "Virtual"
image: "/images/qrgjuz/slide_000.jpg"
pdf: "/pdfs/qrgjuz.pdf"
notist_id: "qrgjuz"
resources:
  - title: "Confluent Cloud"
    url: "https://www.confluent.io/confluent-cloud/tryfree/"
    description: "Managed Apache Kafka, ksqlDB, and Schema Registry. Use code RMOFF200 when you sign up!"
  - title: "Confluent Developer"
    url: "https://developer.confluent.io"
    description: "The pre-eminent resource for learning Apache Kafka. There are free training courses, event streaming patterns, deep-dive articles, and language-specific client programming guides. Check it out!"
  - title: "✍🏻Blog: Streaming ETL and Analytics on Confluent with Maritime AIS Data"
    url: "https://www.confluent.io/blog/streaming-etl-and-analytics-for-real-time-location-tracking"
  - title: "✍🏻Blog: Detecting Patterns of Behaviour in Streaming Maritime AIS Data with Confluent"
    url: "https://www.confluent.io/blog/streaming-data-with-confluent-and-ksqldb-for-new-use-cases-with-ais/"
  - title: "👾Demo code"
    url: "https://github.com/confluentinc/demo-scene/tree/master/maritime-ais"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">That was my favorite talk so far at the Summit. Thank you for preparing and presenting this one, Robin. It was awesome. First time that I see the power of ksql being used in a practical way.</p>&mdash; Brian (@bdicroce) <a href="https://twitter.com/bdicroce/status/1437861680655081478?ref_src=twsrc%5Etfw">September 14, 2021</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Interesting use-case presented by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> at <a href="https://twitter.com/hashtag/KafkaSummit2021?src=hash&amp;ref_src=twsrc%5Etfw">#KafkaSummit2021</a> <a href="https://t.co/USBevRnDW7">https://t.co/USBevRnDW7</a></p>&mdash; David P. (@davpow) <a href="https://twitter.com/davpow/status/1437859564012154880?ref_src=twsrc%5Etfw">September 14, 2021</a></blockquote>
  - type: "notist_video"
    html: |
      <iframe sandbox="allow-scripts allow-same-origin allow-presentation" allowfullscreen class="embedded-deck embedded-video"
                          src="https://notist.ninja/embed/UuRQsv"></iframe>
---

<p><strong>This is the recording of my Kafka Summit 2021 talk about doing interesting things with real-time streams of AIS data. It covers both “standard” streaming ETL stuff to build fancy dashboards, as well as using stream processing to identify in real-time ships that may be engaged in transshipping.</strong></p>
<p><strong>If you’re interested in the topic but prefer the written word to video, the talk is based on <a href="https://www.confluent.io/blog/streaming-etl-and-analytics-for-real-time-location-tracking" target="_blank" rel="noopener">these</a> <a href="https://www.confluent.io/blog/streaming-data-with-confluent-and-ksqldb-for-new-use-cases-with-ais/" target="_blank" rel="noopener">two</a> blogs.</strong></p>
<hr />
<blockquote>
<p><em>The great thing about streams of real-time events is that they can be used to spot behaviours as they happen and respond to them as needed. Instead of waiting until tomorrow to find out what happened yesterday, we can act on things straight away.</em></p>
</blockquote>
<blockquote>
<p><em>This talk will show a real-life example of one particular pattern that it’s useful to detect—ships engaged in potentially suspicious behaviour at sea. Transhipping is often used for legitimate purposes to optimise efficiencies but can also be used for nefarious purposes such as illegal fishing.</em></p>
</blockquote>
<blockquote>
<p><em>By capturing streams of maritime AIS data in real-time into Kafka and processing it with ksqlDB, it’s possible to detect the kind of characteristics that could indicate behaviour of interest, such as ships moving slowly at close proximity for a length of time.</em></p>
</blockquote>
<blockquote>
<p><em>I’ll demonstrate how the data was ingested from a raw TCP feed, unified with reference data from CSV files, and then processed to spot patterns with the resulting real-time stream of matches written to a new Kafka topic for validation and analysis.</em></p>
</blockquote>
