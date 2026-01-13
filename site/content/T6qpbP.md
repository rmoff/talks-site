---
title: "🚂 On Track with Apache Kafka: Building a Streaming ETL solution with Rail Data"
slug: "on-track-with-apache-kafka-building-a-streaming-etl-solution-with-rail-data-T6qpbP"
date: 2021-11-01T08:00:00
event: "Devoxx UK"
location: "London, UK"
image: "/images/T6qpbP/slide_000.jpg"
pdf: "/pdfs/T6qpbP.pdf"
notist_id: "T6qpbP"
resources:
  - title: "✍️ Blog - 🚂 On Track with Apache Kafka – Building a Streaming ETL Solution with Rail Data"
    url: "https://www.confluent.co.uk/blog/build-streaming-etl-solutions-with-kafka-and-rail-data/?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_devoxxuk2021-2021-11-02&utm_term=rmoff-devx"
  - title: "👾 Demo code"
    url: "https://github.com/confluentinc/demo-scene/tree/master/rail-data-streaming-pipeline"
  - title: "☁️Confluent Cloud☁️"
    url: "https://www.confluent.io/confluent-cloud/tryfree?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_devoxxuk2021-2021-11-02&utm_term=rmoff-devx"
    description: "Managed Apache Kafka, ksqlDB, and Schema Registry. Use code RMOFF200 when you sign up!"
  - title: "Confluent Developer"
    url: "https://developer.confluent.io/?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_devoxxuk2021-2021-11-02&utm_term=rmoff-devx"
    description: "The pre-eminent resource for learning Apache Kafka. Free training courses, event streaming patterns, deep-dive articles, and language-specific client programming guides. Check it out!"
  - title: "Apache Kafka 101 - free training course"
    url: "https://developer.confluent.io/learn-kafka/apache-kafka/?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_devoxxuk2021-2021-11-02&utm_term=rmoff-devx"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/devoxxuk?src=hash&amp;ref_src=twsrc%5Etfw">#devoxxuk</a> <a href="https://twitter.com/hashtag/speakerselfie?src=hash&amp;ref_src=twsrc%5Etfw">#speakerselfie</a> <a href="https://twitter.com/hashtag/streamingselfie?src=hash&amp;ref_src=twsrc%5Etfw">#streamingselfie</a> <a href="https://t.co/qoiQefC6Ry">pic.twitter.com/qoiQefC6Ry</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1455511049868873735?ref_src=twsrc%5Etfw">November 2, 2021</a></blockquote>
---

<p>As data engineers, we frequently need to build scalable systems working with data from a variety of sources and with various ingest rates, sizes, and formats. This talk takes an in-depth look at how Apache Kafka can be used to provide a common platform on which to build data infrastructure driving both real-time analytics as well as event-driven applications.</p>
<p>Using a public feed of railway data it will show how to ingest data from message queues such as ActiveMQ with Kafka Connect, as well as from static sources such as S3 and REST endpoints. We’ll then see how to use stream processing to transform the data into a form useful for streaming to analytics in tools such as Elasticsearch and Neo4j. The same data will be used to drive a real-time notifications service through Telegram.</p>
<p>If you’re wondering how to build your next scalable data platform, how to reconcile the impedance mismatch between stream and batch, and how to wrangle streams of data—this talk is for you!</p>
