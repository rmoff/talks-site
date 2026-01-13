---
title: "🤖 Building a Telegram bot with Apache Kafka, Go, and ksqlDB"
slug: "building-a-telegram-bot-with-apache-kafka-go-and-ksqldb-AIv0A7"
date: 2021-03-10T08:00:00
event: "Blueprint LDN"
location: "Virtual"
image: "/images/AIv0A7/slide_000.jpg"
pdf: "/pdfs/AIv0A7.pdf"
notist_id: "AIv0A7"
resources:
  - title: "Confluent Developer"
    url: "https://developer.confluent.io?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_blueprintldn-2021-03-10&utm_term=rmoff-devx"
    description: "Your destination for learning all about Confluent—Tutorials, examples, documentation, blogs, podcasts, and lots more!"
  - title: "👾Code for you to try the full demo yourself"
    url: "https://github.com/confluentinc/demo-scene/tree/master/telegram-bot-carparks"
    description: "The demo is built on Docker so anyone can easily spin it up and give it a try."
  - title: "☁️Confluent Cloud"
    url: "https://www.confluent.io/confluent-cloud/tryfree?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_blueprintldn-2021-03-10&utm_term=rmoff-devx"
    description: "Fully Managed Apache Kafka, Schema Registry, ksqlDB, and Connectors. Use promo code RMOFF200 to get an additional $200 of free Confluent Cloud usage. Be sure to activate it by June 30 2021, and to use it within 90 days after activation. Any unused promo value on the expiration date will be forfeited and there are a limited number of codes available, so don’t miss out!"
  - title: "📌 Kafka as a Platform: the Ecosystem from the Ground Up"
    url: "https://rmoff.dev/kafka101"
  - title: "🎥 Kafka Connect tutorials on YouTube"
    url: "http://youtube.com/rmoff"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/SpeakerSelfie?src=hash&amp;ref_src=twsrc%5Etfw">#SpeakerSelfie</a> <a href="https://twitter.com/LDN_Blueprint?ref_src=twsrc%5Etfw">@LDN_Blueprint</a> <a href="https://t.co/0j1hIJGOlI">pic.twitter.com/0j1hIJGOlI</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1369616533283086339?ref_src=twsrc%5Etfw">March 10, 2021</a></blockquote>
---

<p>Imagine you’ve got a stream of data; it’s not “big data,” but it’s certainly a lot. Within the data, you’ve got some bits you’re interested in, and of those bits, you’d like to be able to query information about them at any point. Sounds fun, right? Since I mentioned “querying,” I’d hazard a guess that you’ve got in mind an additional datastore of some sort, whether relational or NoSQL.</p>
<p>But what if I told you…that you didn’t need any datastore other than Kafka itself? What if you could ingest, filter, enrich, aggregate, and query data with just Kafka? With ksqlDB we can do just this, and I want to show you exactly how.</p>
<p>In this hands-on talk we’ll walk through an example of building a Telegram bot in which ksqlDB provides the key/value lookups driven by a materialised view on the stream of events in Kafka. We’ll take a look at what ksqlDB is and its capabilities for processing data and driving applications, as well as integrating with other systems.</p>
