---
title: "🚂 On Track with Apache Kafka: Building a Streaming ETL solution with Rail Data"
slug: "on-track-with-apache-kafka-building-a-streaming-etl-solution-with-rail-data-A9nZm9"
aliases: ["/A9nZm9/on-track-with-apache-kafka-building-a-streaming-etl-solution-with-rail-data"]
date: 2021-07-27T08:00:00
event: "Kafka Summit APAC"
location: "Virtual"
image: "/images/A9nZm9/slide_000.jpg"
pdf: "/pdfs/A9nZm9.pdf"
notist_id: "A9nZm9"
resources:
  - title: "👾Code"
    url: "https://github.com/confluentinc/demo-scene/blob/master/rail-data-streaming-pipeline/"
    description: "Try out the code shown in this talk using Docker"
  - title: "Confluent Cloud"
    url: "https://www.confluent.io/confluent-cloud/tryfree?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_kafkasummitapac-2021-07-28&utm_term=rmoff-devx"
    description: "Confluent Cloud provides fully managed Apache Kafka, connectors, Schema Registry, and ksqlDB. Try it out and use code RMOFF200 for money off your bill ( T&amp;C )"
  - title: "✍️ Blog"
    url: "https://www.confluent.io/blog/build-streaming-etl-solutions-with-kafka-and-rail-data/"
    description: "This blog is a write up of the material covered in this talk"
  - title: "🎥 Recording"
    url: "https://www.confluent.io/events/kafka-summit-europe-2021/on-track-with-apache-kafka-building-a-streaming-etl-solution-with-rail-data/"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/KafkaSummit?src=hash&amp;ref_src=twsrc%5Etfw">#KafkaSummit</a> <a href="https://twitter.com/hashtag/speakerselfie?src=hash&amp;ref_src=twsrc%5Etfw">#speakerselfie</a> <a href="https://twitter.com/hashtag/streamingselfie?src=hash&amp;ref_src=twsrc%5Etfw">#streamingselfie</a> <a href="https://t.co/de0av2nWMI">https://t.co/de0av2nWMI</a> <a href="https://t.co/1OtYf4NJOm">pic.twitter.com/1OtYf4NJOm</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1420263860771164162?ref_src=twsrc%5Etfw">July 28, 2021</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">I&#39;m currently watching your talk - I&#39;m going to have a go at having a play with this myself!</p>&mdash; Lju Lazarevic (@ElLazal) <a href="https://twitter.com/ElLazal/status/1420266418772250625?ref_src=twsrc%5Etfw">July 28, 2021</a></blockquote>
---

<p>As data engineers, we frequently need to build scalable systems working with data from a variety of sources and with various ingest rates, sizes, and formats. This talk takes an in-depth look at how Apache Kafka can be used to provide a common platform on which to build data infrastructure driving both real-time analytics as well as event-driven applications.</p>
<p>Using a public feed of railway data it will show how to ingest data from message queues such as ActiveMQ with Kafka Connect, as well as from static sources such as S3 and REST endpoints. We’ll then see how to use stream processing to transform the data into a form useful for streaming to analytics in tools such as Elasticsearch and Neo4j. The same data will be used to drive a real-time notifications service through Telegram.</p>
<p>If you’re wondering how to build your next scalable data platform, how to reconcile the impedance mismatch between stream and batch, and how to wrangle streams of data—this talk is for you!</p>
