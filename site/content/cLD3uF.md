---
title: "ETL 2.0: It’s not just for data engineers anymore"
slug: "etl-2-0-its-not-just-for-data-engineers-anymore-cLD3uF"
aliases: ["/cLD3uF/etl-2-0-its-not-just-for-data-engineers-anymore"]
date: 2019-11-04T08:00:00
event: "O’Reilly Software Architecture Conference"
location: "Berlin, Germany"
image: "/images/cLD3uF/slide_000.jpg"
pdf: "/pdfs/cLD3uF.pdf"
notist_id: "cLD3uF"
resources:
  - title: "📚Free eBooks (including “Kafka: The Definitive Guide”)"
    url: "http://cnfl.io/book-bundle"
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud"
  - title: "💬Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: " ✉️Confluent Community mailing list"
    url: "https://groups.google.com/forum/#!forum/confluent-platform"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Another great talk by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> on use cases of kafka and why we need to change our mindset when we manage data. <a href="https://twitter.com/OReillySACon?ref_src=twsrc%5Etfw">@OReillySACon</a> <a href="https://twitter.com/hashtag/velocityconf?src=hash&amp;ref_src=twsrc%5Etfw">#velocityconf</a> <a href="https://t.co/wG6mQxk8GK">pic.twitter.com/wG6mQxk8GK</a></p>&mdash; curios🐝 @VelocityConf (@ebrucucen) <a href="https://twitter.com/ebrucucen/status/1192454855182503937?ref_src=twsrc%5Etfw">November 7, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Kafka allows you with ksql to mutate a stream and create a derived stream, perhaps cleaner or more fitting for what you do</p>&mdash; Alon Nisser (@alonisser) <a href="https://twitter.com/alonisser/status/1192448760695205889?ref_src=twsrc%5Etfw">November 7, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Now in <a href="https://twitter.com/OReillySACon?ref_src=twsrc%5Etfw">@OReillySACon</a> , <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> on etl, streaming, etc with Kafka. &quot;Kafka is new, if you built things like you did before it wouldn&#39;t end well&quot;</p>&mdash; Alon Nisser (@alonisser) <a href="https://twitter.com/alonisser/status/1192447974888157184?ref_src=twsrc%5Etfw">November 7, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Made it! <a href="https://twitter.com/hashtag/OReillySACon?src=hash&amp;ref_src=twsrc%5Etfw">#OReillySACon</a> <a href="https://t.co/fRKrvlNWS4">https://t.co/fRKrvlNWS4</a> <a href="https://t.co/xgj0pVwY6r">pic.twitter.com/xgj0pVwY6r</a></p>&mdash; Robin Moffatt @ 🇩🇰 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1192433000383995905?ref_src=twsrc%5Etfw">November 7, 2019</a></blockquote>
---

<p>Developers have long employed message queues to decouple subsystems and provide an approximation of asynchronous processing. But these legacy queuing systems don’t adequately deliver on the promise of event-driven architectures and often lead to contrived integration patterns. Their limited scalability and durability limit you in using events to their full potential. Events carry both notification and state and form a powerful primitive upon which to build systems for developers and data engineers alike. Developers benefit from the asynchronous communication that events enable between services, and data engineers benefit from the integration capabilities. Everyone gains from using the standards-based, scalable, and resilient streaming platform.</p>
<p>Robin Moffatt explores the concepts of events, their relevance to software and data engineers, and their powers for unifying architectures in a powerful way. You’ll see how stream processing makes sense in both a microservices and ETL environment, and how ETL is actually more common than you may think. Robin provides a hands-on demonstration of these concepts in practice using Apache Kafka and commentary on the design choices made.</p>
