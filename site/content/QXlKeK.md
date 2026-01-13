---
title: "Kafka as a Platform: the Ecosystem from the Ground Up"
slug: "kafka-as-a-platform-the-ecosystem-from-the-ground-up-QXlKeK"
date: 2021-09-21T00:00:00
event: "ApacheCon"
location: "Virtual"
image: "/images/QXlKeK/slide_000.jpg"
pdf: "/pdfs/QXlKeK.pdf"
notist_id: "QXlKeK"
resources:
  - title: "Confluent Cloud"
    url: "https://www.confluent.io/confluent-cloud/tryfree/"
    description: "Managed Apache Kafka, ksqlDB, and Schema Registry. Use code RMOFF200 when you sign up!"
  - title: "Confluent Developer"
    url: "https://developer.confluent.io"
    description: "The pre-eminent resource for learning Apache Kafka. There are free training courses, event streaming patterns, deep-dive articles, and language-specific client programming guides. Check it out!"
  - title: "Apache Kafka 101"
    url: "https://developer.confluent.io/learn-kafka/apache-kafka/"
    description: "Free training course"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/acah2021?src=hash&amp;ref_src=twsrc%5Etfw">#acah2021</a> <a href="https://twitter.com/ApacheCon?ref_src=twsrc%5Etfw">@apachecon</a> <a href="https://twitter.com/hashtag/speakerselfie?src=hash&amp;ref_src=twsrc%5Etfw">#speakerselfie</a> <a href="https://twitter.com/hashtag/streamingselfie?src=hash&amp;ref_src=twsrc%5Etfw">#streamingselfie</a> <a href="https://t.co/9e5ELT8Q6G">pic.twitter.com/9e5ELT8Q6G</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1440374292529643535?ref_src=twsrc%5Etfw">September 21, 2021</a></blockquote>
---

<p>Kafka has become a key data infrastructure technology, and we all have at least a vague sense that it is a messaging system, but what else is it? How can an overgrown message bus be getting this much buzz? Well, because Kafka is merely the center of a rich streaming data platform that invites detailed exploration.</p>
<p>In this talk, we’ll look at the entire streaming platform provided by Apache Kafka and the Confluent community components. Starting with a lonely key-value pair, we’ll build up topics, partitioning, replication, and low-level Producer and Consumer APIs. We’ll group consumers into elastically scalable, fault-tolerant application clusters, then layer on more sophisticated stream processing APIs like Kafka Streams and ksqlDB. We’ll help teams collaborate around data formats with schema management. We’ll integrate with legacy systems without writing custom code. By the time we’re done, the open-source project we thought was Big Data’s answer to message queues will have become an enterprise-grade streaming platform, all in 50 minutes.</p>
