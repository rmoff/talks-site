---
title: "From Zero to Hero with Kafka Connect"
slug: "from-zero-to-hero-with-kafka-connect-UmOkou"
date: 2020-02-24T08:00:00
event: "BruJUG / Apache Kafka meetup"
location: "Brussels, Belgium"
image: "/images/UmOkou/slide_000.png"
pdf: "/pdfs/UmOkou.pdf"
notist_id: "UmOkou"
resources:
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud/signup"
    description: "Fully Managed Apache Kafka, Schema Registry, KSQL, and Connectors"
  - title: "📚Free eBooks"
    url: "https://rmoff.dev/BruJUG"
    description: "Free eBooks to download, including Kafka: The Definitive Guide."
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "👾 Demo code"
    url: "https://rmoff.dev/brujug20-code"
    description: "All you need is Docker &amp; Docker Compose!"
  - title: "🎥 Recording"
    url: "https://videos.confluent.io/watch/wyc1oqmkoQj4k5WM9CuAwg?"
    description: "Same talk, different occassion."
  - title: "🖼️No More Silos: Integrating Databases and Apache Kafka"
    url: "http://rmoff.dev/ksny19-no-more-silos"
    description: "The ins and outs of streaming data from RDBMS into Kafka, including how to choose between query-based CDC (JDBC Source connector) and log-based CDC (e.g. Debezium, GoldenGate, etc)"
  - title: "🖼️The Changing Face of ETL: Event-Driven Architectures for Data Engineers"
    url: "https://talks.rmoff.net/Jn6rgo/the-changing-face-of-etl-event-driven-architectures-for-data-engineers"
  - title: "✍️Kafka Connect Deep Dive – Converters and Serialization Explained"
    url: "https://www.confluent.io/blog/kafka-connect-deep-dive-converters-serialization-explained/"
  - title: "✍️Kafka Connect Deep Dive – Error Handling and Dead Letter Queues"
    url: "https://www.confluent.io/blog/kafka-connect-deep-dive-error-handling-dead-letter-queues/"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">From Zero to Hero with <a href="https://twitter.com/hashtag/Kafka?src=hash&amp;ref_src=twsrc%5Etfw">#Kafka</a> <a href="https://twitter.com/hashtag/Connect?src=hash&amp;ref_src=twsrc%5Etfw">#Connect</a> by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> at <a href="https://twitter.com/BruJUG?ref_src=twsrc%5Etfw">@BruJUG</a> <br><br>What a great piece of “glue” <a href="https://twitter.com/confluentinc?ref_src=twsrc%5Etfw">@confluentinc</a> :) <a href="https://t.co/kyntCoQE99">pic.twitter.com/kyntCoQE99</a></p>&mdash; Ricardo Moreira (@_ramoreira) <a href="https://twitter.com/_ramoreira/status/1232007695315722240?ref_src=twsrc%5Etfw">February 24, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">And the show starts ! <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> on stage for <a href="https://twitter.com/hashtag/kafka?src=hash&amp;ref_src=twsrc%5Etfw">#kafka</a> <a href="https://twitter.com/hashtag/connect?src=hash&amp;ref_src=twsrc%5Etfw">#connect</a><br>Thanks to <a href="https://twitter.com/confluentinc?ref_src=twsrc%5Etfw">@confluentinc</a> for sponsoring and providing food to all those attendees 🙏 <a href="https://t.co/iBfN9c5LVH">pic.twitter.com/iBfN9c5LVH</a></p>&mdash; Brussels Java UG (@BruJUG) <a href="https://twitter.com/BruJUG/status/1232008062279520256?ref_src=twsrc%5Etfw">February 24, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Advice when using Kafka connect: choose your schema wisely 😅 <a href="https://t.co/g85a5NVt8s">pic.twitter.com/g85a5NVt8s</a></p>&mdash; Brussels Java UG (@BruJUG) <a href="https://twitter.com/BruJUG/status/1232015630649430017?ref_src=twsrc%5Etfw">February 24, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="pl" dir="ltr">From Zero to Hero with Kafka Connect 🤓 <a href="https://t.co/V27RcLxGcJ">pic.twitter.com/V27RcLxGcJ</a></p>&mdash; Sam (@s_debruyn) <a href="https://twitter.com/s_debruyn/status/1232007829470531590?ref_src=twsrc%5Etfw">February 24, 2020</a></blockquote>
---

<p>Integrating Apache Kafka with other systems in a reliable and scalable way is often a key part of a streaming platform. Fortunately, Apache Kafka includes the Connect API that enables streaming integration both in and out of Kafka. Like any technology, understanding its architecture and deployment patterns is key to successful use, as is knowing where to go looking when things aren’t working.</p>
<p>This talk will discuss the key design concepts within Kafka Connect and the pros and cons of standalone vs distributed deployment modes. We’ll do a live demo of building pipelines with Kafka Connect for streaming data in from databases, and out to targets including Elasticsearch. With some gremlins along the way, we’ll go hands-on in methodically diagnosing and resolving common issues encountered with Kafka Connect. The talk will finish off by discussing more advanced topics including Single Message Transforms, and deployment of Kafka Connect in containers.</p>
