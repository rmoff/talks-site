---
title: "🚂 On Track with Apache Kafka: Building a Streaming ETL solution with Rail Data"
slug: "on-track-with-apache-kafka-building-a-streaming-etl-solution-with-rail-data-6GsyFX"
aliases: ["/6GsyFX/on-track-with-apache-kafka-building-a-streaming-etl-solution-with-rail-data"]
date: 2021-05-11T08:00:00
event: "Kafka Summit Europe 2021"
location: "Virtual"
image: "/images/6GsyFX/slide_000.jpg"
pdf: "/pdfs/6GsyFX.pdf"
notist_id: "6GsyFX"
resources:
  - title: "👾Code"
    url: "https://github.com/confluentinc/demo-scene/blob/master/rail-data-streaming-pipeline/"
    description: "Try out the code shown in this talk using Docker"
  - title: "Confluent Cloud"
    url: "https://www.confluent.io/confluent-cloud/tryfree?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_kafkasummit-2021-05-12&utm_term=rmoff-devx"
    description: "Confluent Cloud provides fully managed Apache Kafka, connectors, Schema Registry, and ksqlDB. Try it out and use code RMOFF200 for money off your bill ( T&amp;C )"
  - title: "✍️ Blog"
    url: "https://www.confluent.io/blog/build-streaming-etl-solutions-with-kafka-and-rail-data/"
    description: "This blog is a write up of the material covered in this talk"
  - title: "🎥 Recording"
    url: "https://www.confluent.io/events/kafka-summit-europe-2021/on-track-with-apache-kafka-building-a-streaming-etl-solution-with-rail-data/"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Making my way through <a href="https://twitter.com/hashtag/kafkasummit?src=hash&amp;ref_src=twsrc%5Etfw">#kafkasummit</a> content. Do check out <a href="https://twitter.com/confluentinc?ref_src=twsrc%5Etfw">@confluentinc</a>’s <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> presentation “🚂 On Track with Apache Kafka: Building a Streaming ETL Solution with Rail Data”. Pragmatic, complete, elegant - a few words that come to mind to describe this talk.</p>&mdash; Neil Buesing (@nbuesing) <a href="https://twitter.com/nbuesing/status/1393529003957538819?ref_src=twsrc%5Etfw">May 15, 2021</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">This is one of the coolest projects I&#39;ve seen shown. <a href="https://t.co/sP41mTBkE5">https://t.co/sP41mTBkE5</a></p>&mdash; Zach McCoy (@ZachAMcCoy) <a href="https://twitter.com/ZachAMcCoy/status/1392960314778525700?ref_src=twsrc%5Etfw">May 13, 2021</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Live now at <a href="https://twitter.com/hashtag/kafkasummit?src=hash&amp;ref_src=twsrc%5Etfw">#kafkasummit</a>! Join at <a href="https://t.co/zMgUN4LxmM">https://t.co/zMgUN4LxmM</a><a href="https://twitter.com/hashtag/speakerselfie?src=hash&amp;ref_src=twsrc%5Etfw">#speakerselfie</a> <a href="https://twitter.com/hashtag/streamingselfie?src=hash&amp;ref_src=twsrc%5Etfw">#streamingselfie</a> <a href="https://t.co/bVIiBaFilv">pic.twitter.com/bVIiBaFilv</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1392434321093500934?ref_src=twsrc%5Etfw">May 12, 2021</a></blockquote>
---

<p>As data engineers, we frequently need to build scalable systems working with data from a variety of sources and with various ingest rates, sizes, and formats. This talk takes an in-depth look at how Apache Kafka can be used to provide a common platform on which to build data infrastructure driving both real-time analytics as well as event-driven applications.</p>
<p>Using a public feed of railway data it will show how to ingest data from message queues such as ActiveMQ with Kafka Connect, as well as from static sources such as S3 and REST endpoints. We’ll then see how to use stream processing to transform the data into a form useful for streaming to analytics in tools such as Elasticsearch and Neo4j. The same data will be used to drive a real-time notifications service through Telegram.</p>
<p>If you’re wondering how to build your next scalable data platform, how to reconcile the impedance mismatch between stream and batch, and how to wrangle streams of data—this talk is for you!</p>
