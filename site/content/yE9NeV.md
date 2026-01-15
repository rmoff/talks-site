---
title: "From Zero to Hero with Kafka Connect"
slug: "from-zero-to-hero-with-kafka-connect-yE9NeV"
aliases: ["/yE9NeV/from-zero-to-hero-with-kafka-connect"]
date: 2019-06-17T08:00:00
event: "Berlin Buzzwords 2019"
location: "Berlin, Germany"
image: "/images/yE9NeV/slide_000.png"
pdf: "/pdfs/yE9NeV.pdf"
notist_id: "yE9NeV"
resources:
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "👾 Demo code"
    url: "https://github.com/confluentinc/demo-scene/tree/master/kafka-connect-zero-to-hero"
  - title: "🎥 Recording"
    url: "https://videos.confluent.io/watch/wyc1oqmkoQj4k5WM9CuAwg?"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Amazing talk by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> on <a href="https://twitter.com/hashtag/kafkaconnect?src=hash&amp;ref_src=twsrc%5Etfw">#kafkaconnect</a>, touching serialization issues and other common troubleshooting points. Also good that I can finally put an accent on those tweets! <a href="https://twitter.com/hashtag/bbuzz?src=hash&amp;ref_src=twsrc%5Etfw">#bbuzz</a> <a href="https://t.co/aQMbb0Vj76">pic.twitter.com/aQMbb0Vj76</a></p>&mdash; morsapaes (@morsapaes) <a href="https://twitter.com/morsapaes/status/1140650851230507009?ref_src=twsrc%5Etfw">June 17, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Amazing talk by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> about Kafka Connect at <a href="https://twitter.com/hashtag/bbuzz?src=hash&amp;ref_src=twsrc%5Etfw">#bbuzz</a> very well explained, it was a very interesting talk, <a href="https://t.co/5GR3LKWFfA">pic.twitter.com/5GR3LKWFfA</a></p>&mdash; Alejandro Pérez L. @ #bbuzz (@alexperezl) <a href="https://twitter.com/alexperezl/status/1140650680832659459?ref_src=twsrc%5Etfw">June 17, 2019</a></blockquote>
---

<p>Integrating Apache Kafka with other systems in a reliable and scalable way is often a key part of a streaming platform. Fortunately, Apache Kafka includes the Connect API that enables streaming integration both in and out of Kafka. Like any technology, understanding its architecture and deployment patterns is key to successful use, as is knowing where to go looking when things aren’t working.</p>
<p>This talk will discuss the key design concepts within Kafka Connect and the pros and cons of standalone vs distributed deployment modes. We’ll do a live demo of building pipelines with Kafka Connect for streaming data in from databases, and out to targets including Elasticsearch. With some gremlins along the way, we’ll go hands-on in methodically diagnosing and resolving common issues encountered with Kafka Connect. The talk will finish off by discussing more advanced topics including Single Message Transforms, and deployment of Kafka Connect in containers.</p>
