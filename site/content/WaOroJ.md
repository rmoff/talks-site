---
title: "Streaming ETL in Practice with Oracle, Apache Kafka, and KSQL"
slug: "streaming-etl-in-practice-with-oracle-apache-kafka-and-ksql-WaOroJ"
date: 2019-06-24T08:00:00
event: "KScope 19"
location: "Seattle, WA, USA"
image: "/images/WaOroJ/slide_000.jpg"
pdf: "/pdfs/WaOroJ.pdf"
notist_id: "WaOroJ"
resources:
  - title: "👾 Demo code"
    url: "https://github.com/confluentinc/demo-scene/blob/master/oracle-ksql-elasticsearch/demo_oracle-streaming-etl.adoc"
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "📚Free eBooks (including “Kafka: The Definitive Guide”)"
    url: "http://cnfl.io/book-bundle"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Awesome session on Streaming ETL in Practice with Oracle, Apache Kafka, and KSQL by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> <a href="https://twitter.com/hashtag/kscope19?src=hash&amp;ref_src=twsrc%5Etfw">#kscope19</a> <a href="https://twitter.com/hashtag/Kafka?src=hash&amp;ref_src=twsrc%5Etfw">#Kafka</a> <a href="https://twitter.com/confluentinc?ref_src=twsrc%5Etfw">@confluentinc</a> <a href="https://twitter.com/hashtag/OrclDB?src=hash&amp;ref_src=twsrc%5Etfw">#OrclDB</a> <a href="https://t.co/KJ0oUaYmjd">pic.twitter.com/KJ0oUaYmjd</a></p>&mdash; Alfredo Abate (@HeyAlfredoDBA) <a href="https://twitter.com/HeyAlfredoDBA/status/1143935854890536961?ref_src=twsrc%5Etfw">June 26, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">‘Feeding the terminators’ <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> at <a href="https://twitter.com/hashtag/kscope19?src=hash&amp;ref_src=twsrc%5Etfw">#kscope19</a> explaining why we don’t need to wait for batches to access our data. <a href="https://t.co/eh2wb257H5">pic.twitter.com/eh2wb257H5</a></p>&mdash; Becky Wagner (@Bec_Wagner) <a href="https://twitter.com/Bec_Wagner/status/1143918423820263424?ref_src=twsrc%5Etfw">June 26, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Robin is getting started! Room 310 <a href="https://twitter.com/hashtag/kscope19?src=hash&amp;ref_src=twsrc%5Etfw">#kscope19</a> <a href="https://t.co/RL4KAJrA14">pic.twitter.com/RL4KAJrA14</a></p>&mdash; Becky Wagner (@Bec_Wagner) <a href="https://twitter.com/Bec_Wagner/status/1143912457016004609?ref_src=twsrc%5Etfw">June 26, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Goooooooooood morning <a href="https://twitter.com/hashtag/Kscope19?src=hash&amp;ref_src=twsrc%5Etfw">#Kscope19</a>! Head to room 310 at 09:00 for “Streaming ETL in Practice with Oracle, Apache Kafka, and KSQL” <a href="https://t.co/ArXOjPI7V7">pic.twitter.com/ArXOjPI7V7</a></p>&mdash; 𝚁𝚘𝚋𝚒𝚗 𝙼𝚘𝚏𝚏𝚊𝚝𝚝 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1143885309072953344?ref_src=twsrc%5Etfw">June 26, 2019</a></blockquote>
---

<p>Have you ever thought that you needed to be a programmer to do stream processing and build streaming data pipelines? Think again!</p>
<p>Companies new and old are all recognizing the importance of a low-latency, scalable, fault-tolerant data backbone in the form of the Apache Kafka streaming platform. With Kafka, developers can integrate multiple sources and systems, which enables low-latency analytics, event-driven architectures, and the population of multiple downstream systems. These data pipelines can be built using configuration alone.</p>
<p>In this talk, we’ll see how easy it is to stream data from a database such as Oracle into Kafka using CDC and Kafka Connect. In addition, we’ll use KSQL to filter, aggregate, and join it to other data, and then stream this from Kafka out into multiple targets such as Elasticsearch and S3. All of this can be accomplished without a single line of code!</p>
<p>Why should Java geeks have all the fun?</p>
