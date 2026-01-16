---
title: "🚂 On Track with Apache Kafka: Building a Streaming ETL solution with Rail Data"
slug: "on-track-with-apache-kafka-building-a-streaming-etl-solution-with-rail-data-51cZrz"
date: 2021-03-22T08:00:00
event: "Apache Kafka Meetup"
location: "Virtual"
image: "/images/51cZrz/slide_000.jpg"
pdf: "/pdfs/51cZrz.pdf"
notist_id: "51cZrz"
resources:
  - title: "Confluent Cloud"
    url: "https://www.confluent.io/confluent-cloud/tryfree?utm_source=meetup&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_stockholm-2021-03-22&utm_term=rmoff-devx"
    description: "Coupon code: RMOFF200 (T&amp;C: https://www.confluent.io/confluent-cloud-promo-disclaimer)"
  - title: "👾 Code"
    url: "https://github.com/confluentinc/demo-scene/tree/master/rail-data-streaming-pipeline"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/SpeakerSelfie?src=hash&amp;ref_src=twsrc%5Etfw">#SpeakerSelfie</a> <a href="https://t.co/dcxbUMOXHq">https://t.co/dcxbUMOXHq</a> <a href="https://t.co/UymWyarCyd">pic.twitter.com/UymWyarCyd</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1374045370720923655?ref_src=twsrc%5Etfw">March 22, 2021</a></blockquote>
---

<p>As data engineers, we frequently need to build scalable systems working with data from a variety of sources and with various ingest rates, sizes, and formats. This talk takes an in-depth look at how Apache Kafka can be used to provide a common platform on which to build data infrastructure driving both real-time analytics as well as event-driven applications.</p>
<p>Using a public feed of railway data it will show how to ingest data from message queues such as ActiveMQ with Kafka Connect, as well as from static sources such as S3 and REST endpoints. We’ll then see how to use stream processing to transform the data into a form useful for streaming to analytics in tools such as Elasticsearch and Neo4j. The same data will be used to drive a real-time notifications service through Telegram.</p>
<p>If you’re wondering how to build your next scalable data platform, how to reconcile the impedance mismatch between stream and batch, and how to wrangle streams of data—this talk is for you!</p>
