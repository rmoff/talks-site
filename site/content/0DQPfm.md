---
title: "From Zero to Hero with Kafka Connect"
slug: "from-zero-to-hero-with-kafka-connect-0DQPfm"
aliases: ["/0DQPfm/from-zero-to-hero-with-kafka-connect"]
date: 2019-10-21T08:00:00
event: "Voxxed Microservices"
location: "Paris, France"
image: "/images/0DQPfm/slide_000.png"
pdf: "/pdfs/0DQPfm.pdf"
notist_id: "0DQPfm"
resources:
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "👾 Demo code"
    url: "https://rmoff.dev/crunchconf19-code"
  - title: "🎥 Recording (same talk, different occassion)"
    url: "https://videos.confluent.io/watch/wyc1oqmkoQj4k5WM9CuAwg?"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Robin Moffatt and his talk &quot;From Zero to Hero with Kafka Connect&quot;<a href="https://twitter.com/hashtag/microservices?src=hash&amp;ref_src=twsrc%5Etfw">#microservices</a> <a href="https://twitter.com/hashtag/Apache?src=hash&amp;ref_src=twsrc%5Etfw">#Apache</a> <a href="https://twitter.com/hashtag/Kafka?src=hash&amp;ref_src=twsrc%5Etfw">#Kafka</a> <a href="https://twitter.com/hashtag/ApacheKafka?src=hash&amp;ref_src=twsrc%5Etfw">#ApacheKafka</a> <a href="https://twitter.com/hashtag/Integration?src=hash&amp;ref_src=twsrc%5Etfw">#Integration</a> <a href="https://twitter.com/hashtag/DataStreaming?src=hash&amp;ref_src=twsrc%5Etfw">#DataStreaming</a> <a href="https://twitter.com/confluent?ref_src=twsrc%5Etfw">@Confluent</a> <a href="https://t.co/9favsm7Z2m">pic.twitter.com/9favsm7Z2m</a></p>&mdash; Voxxed Days Microservices (@vxdmicroservice) <a href="https://twitter.com/vxdmicroservice/status/1186260702102802434?ref_src=twsrc%5Etfw">October 21, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Learning about Kafka Connect from <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> 🤔 <br><br>&quot;Look ma, no code!&quot;<a href="https://twitter.com/vxdmicroservice?ref_src=twsrc%5Etfw">@vxdmicroservice</a> <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@apachekafka</a>  <a href="https://twitter.com/hashtag/voxxedmicroservices?src=hash&amp;ref_src=twsrc%5Etfw">#voxxedmicroservices</a> <a href="https://t.co/lvz7kTtWbo">pic.twitter.com/lvz7kTtWbo</a></p>&mdash; Ania Wyrwinska (@AniaWyrwinska) <a href="https://twitter.com/AniaWyrwinska/status/1186261665773477888?ref_src=twsrc%5Etfw">October 21, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Next!<br><br>From zero to hero with Kafka connect by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> <a href="https://t.co/mAouL9apXQ">https://t.co/mAouL9apXQ</a><a href="https://twitter.com/hashtag/VoxxedMicroservices?src=hash&amp;ref_src=twsrc%5Etfw">#VoxxedMicroservices</a> <a href="https://t.co/2Q2g5NAW8d">pic.twitter.com/2Q2g5NAW8d</a></p>&mdash; Sylvain PONTOREAU (@spontoreau) <a href="https://twitter.com/spontoreau/status/1186258299991330816?ref_src=twsrc%5Etfw">October 21, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr"><a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> through kafka connect reality, nice practices and warnings before starting using it in prod. <a href="https://twitter.com/vxdmicroservice?ref_src=twsrc%5Etfw">@vxdmicroservice</a> <a href="https://twitter.com/hashtag/VoxxedMicroservices?src=hash&amp;ref_src=twsrc%5Etfw">#VoxxedMicroservices</a> <a href="https://t.co/6Z3z74IAiM">pic.twitter.com/6Z3z74IAiM</a></p>&mdash; Philippe Anes (@philatdev) <a href="https://twitter.com/philatdev/status/1186269594698371073?ref_src=twsrc%5Etfw">October 21, 2019</a></blockquote>
---

<p>Integrating Apache Kafka with other systems in a reliable and scalable way is often a key part of a streaming platform. Fortunately, Apache Kafka includes the Connect API that enables streaming integration both in and out of Kafka. Like any technology, understanding its architecture and deployment patterns is key to successful use, as is knowing where to go looking when things aren’t working.</p>
<p>This talk will discuss the key design concepts within Kafka Connect and the pros and cons of standalone vs distributed deployment modes. We’ll do a live demo of building pipelines with Kafka Connect for streaming data in from databases, and out to targets including Elasticsearch. With some gremlins along the way, we’ll go hands-on in methodically diagnosing and resolving common issues encountered with Kafka Connect. The talk will finish off by discussing more advanced topics including Single Message Transforms, and deployment of Kafka Connect in containers.</p>
