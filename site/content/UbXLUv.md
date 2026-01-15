---
title: "🤖 Building a Telegram bot with Apache Kafka, Go, and ksqlDB"
slug: "building-a-telegram-bot-with-apache-kafka-go-and-ksqldb-UbXLUv"
aliases: ["/UbXLUv/building-a-telegram-bot-with-apache-kafka-go-and-ksqldb"]
date: 2021-01-25T08:00:00
event: "NDC London 2021"
location: "Virtual"
image: "/images/UbXLUv/slide_000.jpg"
pdf: "/pdfs/UbXLUv.pdf"
notist_id: "UbXLUv"
resources:
  - title: "👾 Code"
    url: "https://rmoff.dev/carparks"
  - title: "🎥 Recording"
    url: ""
    description: "Soon…"
  - title: "☁️Confluent Cloud"
    url: "https://rmoff.dev/ccloud"
    description: "Fully Managed Apache Kafka, Schema Registry, ksqlDB, and Connectors. Use promo code RMOFF200 to get an additional $200 of free Confluent Cloud usage. Be sure to activate it by June 30 2021, and to use it within 90 days after activation. Any unused promo value on the expiration date will be forfeited and there are a limited number of codes available, so don’t miss out!"
  - title: "📌 Kafka as a Platform: the Ecosystem from the Ground Up"
    url: "https://rmoff.dev/kafka101"
  - title: "🎥 Kafka Connect tutorials on YouTube"
    url: "http://youtube.com/rmoff"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/NDCLondon?src=hash&amp;ref_src=twsrc%5Etfw">#NDCLondon</a> <a href="https://twitter.com/hashtag/streamingselfie?src=hash&amp;ref_src=twsrc%5Etfw">#streamingselfie</a> <a href="https://t.co/LwieUt81Cs">pic.twitter.com/LwieUt81Cs</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1354373124255584257?ref_src=twsrc%5Etfw">January 27, 2021</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">The <a href="https://twitter.com/hashtag/DevRel?src=hash&amp;ref_src=twsrc%5Etfw">#DevRel</a> demo gods are not smiling on me today - the <a href="https://twitter.com/hashtag/OpenData?src=hash&amp;ref_src=twsrc%5Etfw">#OpenData</a> API that I&#39;m using for my live demo is kapput. Makes a nice change from it being my own screw up that breaks that demo ;) And at least I&#39;ve discovered _before_ delivering the demo than _during_ 😅</p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1354364842027712512?ref_src=twsrc%5Etfw">January 27, 2021</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Combined with the house next door having the roof replaced, and my internet dropping out halfway through, that was one of my more eventful (geddit?!) virtual conference talks 😬 …  <a href="https://twitter.com/hashtag/NDCLondon?src=hash&amp;ref_src=twsrc%5Etfw">#NDCLondon</a> <a href="https://t.co/Jv9J2QBkRi">https://t.co/Jv9J2QBkRi</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1354389444204367879?ref_src=twsrc%5Etfw">January 27, 2021</a></blockquote>
---

<p>Imagine you’ve got a stream of data; it’s not “big data,” but it’s certainly a lot. Within the data, you’ve got some bits you’re interested in, and of those bits, you’d like to be able to query information about them at any point. Sounds fun, right? Since I mentioned “querying,” I’d hazard a guess that you’ve got in mind an additional datastore of some sort, whether relational or NoSQL.</p>
<p>But what if I told you…that you didn’t need any datastore other than Kafka itself? What if you could ingest, filter, enrich, aggregate, and query data with just Kafka? With ksqlDB we can do just this, and I want to show you exactly how.</p>
<p>In this hands-on talk we’ll walk through an example of building a Telegram bot in which ksqlDB provides the key/value lookups driven by a materialised view on the stream of events in Kafka. We’ll take a look at what ksqlDB is and its capabilities for processing data and driving applications, as well as integrating with other systems.</p>
