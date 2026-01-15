---
title: "Real-time SQL stream processing at scale with Apache Kafka and KSQL"
slug: "real-time-sql-stream-processing-at-scale-with-apache-kafka-and-ksql-3tK7EV"
aliases: ["/3tK7EV/real-time-sql-stream-processing-at-scale-with-apache-kafka-and-ksql"]
date: 2019-04-30T08:00:00
event: "Strata Data Conference, London"
location: "London, UK"
image: "/images/3tK7EV/slide_000.jpg"
pdf: "/pdfs/3tK7EV.pdf"
notist_id: "3tK7EV"
resources:
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "📚Free eBooks (including “Kafka: The Definitive Guide”)"
    url: "http://cnfl.io/book-bundle"
  - title: "💾 Download Confluent Platform"
    url: "https://www.confluent.io/download/"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Assisting <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> at O&#39;Reilly Strata London. Explaining tech content clearly to an audience that&#39;s new to the subject is really, really hard. Watching him at work is a master class. <a href="https://t.co/6HA2AsrzVs">pic.twitter.com/6HA2AsrzVs</a></p>&mdash; Jakub Korab 🇪🇺 (@jakekorab) <a href="https://twitter.com/jakekorab/status/1123142463412211712?ref_src=twsrc%5Etfw">April 30, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Learned a lot today about KSQL during the <a href="https://twitter.com/hashtag/StrataData?src=hash&amp;ref_src=twsrc%5Etfw">#StrataData</a> workshop &quot;Real-time SQL stream processing at scale with <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@ApacheKafka</a> and <a href="https://twitter.com/hashtag/KSQL?src=hash&amp;ref_src=twsrc%5Etfw">#KSQL</a>&quot;. <br>Thanks <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> and <a href="https://twitter.com/jakekorab?ref_src=twsrc%5Etfw">@jakekorab</a> for sharing. <a href="https://t.co/nYYjyne0Aw">pic.twitter.com/nYYjyne0Aw</a></p>&mdash; Sharif Abdel-Halim (@sharif_halim) <a href="https://twitter.com/sharif_halim/status/1123292964816674816?ref_src=twsrc%5Etfw">April 30, 2019</a></blockquote>
---

<p>Have you ever thought that you needed to be a programmer to do stream processing and build streaming data pipelines? Think again. Apache Kafka is a distributed, scalable, and fault-tolerant streaming platform that provides low-latency pub-sub messaging coupled with a native storage and stream processing capabilities. Integrating Kafka with RDBMS, NoSQL, and object stores is simple with Kafka Connect, part of Apache Kafka. KSQL—the open source SQL streaming engine for Apache Kafka—makes it possible to build stream processing applications at scale, written using a familiar SQL interface.</p>
<p>Robin Moffatt walks you through the architectural reasoning for Apache Kafka and the benefits of real-time integration. You’ll then build a streaming data pipeline using nothing but your bare hands, Kafka Connect, and KSQL.</p>
<p>Gasp as you filter events in real time! Be amazed at how we can enrich streams of data with data from RDBMS! Be astonished at the power of streaming aggregates for anomaly detection!</p>
<p>Topics include:</p>
<ul>
<li>Introduction to Apache Kafka (including Kafka Connect for streaming data from databases into Apache Kafka)</li>
<li>Streaming concepts (all data is events; stream/table duality)</li>
<li>Introduction to KSQL</li>
<li>How to run KSQL</li>
<li>Exploring kafka topics in KSQL</li>
<li>Defining KSQL streams and tables over source data</li>
<li>Filtering data in KSQL</li>
<li>Joining data in KSQL</li>
<li>Aggregating data in KSQL</li>
<li>Persisting stream queries</li>
<li>Examining derived Apache Kafka topics</li>
</ul>
