---
title: "The Changing Face of ETL: Event-Driven Architectures for Data Engineers"
slug: "the-changing-face-of-etl-event-driven-architectures-for-data-engineers-A4pLsH"
date: 2019-10-24T08:00:00
event: "Code.Talks"
location: "Hamburg, Germany"
image: "/images/A4pLsH/slide_000.jpg"
pdf: "/pdfs/A4pLsH.pdf"
notist_id: "A4pLsH"
resources:
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "📚Free eBooks (including “Kafka: The Definitive Guide”)"
    url: "http://cnfl.io/book-bundle"
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud"
    description: "Provides managed Apache Kafka, Schema Registry, KSQL, etc"
  - title: "📫 Confluent Community mailing list"
    url: "https://groups.google.com/forum/#!forum/confluent-platform"
  - title: "💾 Download Confluent Platform"
    url: "https://www.confluent.io/download/"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Very inspiring talk by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> about Event Streaming with Apache Kafka <a href="https://twitter.com/hashtag/codetalks?src=hash&amp;ref_src=twsrc%5Etfw">#codetalks</a> <a href="https://twitter.com/hashtag/codetsljs2019?src=hash&amp;ref_src=twsrc%5Etfw">#codetsljs2019</a> <a href="https://twitter.com/hashtag/ApacheKafka?src=hash&amp;ref_src=twsrc%5Etfw">#ApacheKafka</a> <a href="https://t.co/CTA3DQqJ2q">pic.twitter.com/CTA3DQqJ2q</a></p>&mdash; Tschela (@aboalarm_tb) <a href="https://twitter.com/aboalarm_tb/status/1187317342272937991?ref_src=twsrc%5Etfw">October 24, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">That&#39;s what <a href="https://twitter.com/hashtag/codetalks?src=hash&amp;ref_src=twsrc%5Etfw">#codetalks</a> is about, code! Huge code with big letters on a cinema screen. This time: a KSQL query. Showing how you easily process data inside <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@apachekafka</a>. <a href="https://t.co/twxHTlRkJk">pic.twitter.com/twxHTlRkJk</a></p>&mdash; René Kerner (@rk3rn3r) <a href="https://twitter.com/rk3rn3r/status/1187313225265598465?ref_src=twsrc%5Etfw">October 24, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">.<a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> tells you that events are both notification and state transfer in his awesome <a href="https://twitter.com/hashtag/codetalks?src=hash&amp;ref_src=twsrc%5Etfw">#codetalks</a> talk on the &quot;Changing face of ETL&quot; with <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@apachekafka</a>. <a href="https://t.co/iiCcMGIAbT">pic.twitter.com/iiCcMGIAbT</a></p>&mdash; René Kerner (@rk3rn3r) <a href="https://twitter.com/rk3rn3r/status/1187311085428396032?ref_src=twsrc%5Etfw">October 24, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr">👋 <a href="https://t.co/gHi6MZyvlY">pic.twitter.com/gHi6MZyvlY</a></p>&mdash; sudo -u -#1 !! (@invad0r) <a href="https://twitter.com/invad0r/status/1187308176410054662?ref_src=twsrc%5Etfw">October 24, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Popcorn, nachos, and <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@apachekafka</a> ! <a href="https://twitter.com/hashtag/codetalks?src=hash&amp;ref_src=twsrc%5Etfw">#codetalks</a> <a href="https://t.co/jnvLNGw3Hf">pic.twitter.com/jnvLNGw3Hf</a></p>&mdash; Robin Moffatt @ #CodeTalks 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1187307253650595840?ref_src=twsrc%5Etfw">October 24, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Thanks. Nice Talk.</p>&mdash; Philipp Kübler (@MyFrosch) <a href="https://twitter.com/MyFrosch/status/1187307584598007808?ref_src=twsrc%5Etfw">October 24, 2019</a></blockquote>
  - type: "notist_video"
    html: |
      <iframe sandbox="allow-scripts allow-same-origin allow-presentation" allowfullscreen class="embedded-deck embedded-video"
                          src="https://notist.ninja/embed/QcZlkU"></iframe>
---

<p>Data integration in architectures built on static, update-in-place datastores inevitably end up with pathologically high degrees of coupling and poor scalability. This has been the standard practice for decades, as we attempt to build data pipelines on top of databases that do a poor job modeling the fundamental objects that drive our businesses and systems: events.</p>
<p>Events carry both notification and state, and form a powerful primitive on which to build systems for developers and data engineers alike. Developers benefit from the asynchronous communication that events enable between services, and data engineers benefit from the integration capabilities. Everyone gains from using the standards-based, scalable and resilient streaming platform.</p>
<p>In this talk, we’ll discuss the concepts of events, their relevance to both software engineers and data engineers and their ability to unify architectures in a powerful way. We’ll see how stream processing makes sense in both a microservices and ETL environment, and why analytics, data integration and ETL fit naturally into a streaming world.</p>
