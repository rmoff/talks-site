---
title: "🤖 Building a Telegram bot with Apache Kafka and ksqlDB"
slug: "building-a-telegram-bot-with-apache-kafka-and-ksqldb-h7fFAR"
aliases: ["/h7fFAR/building-a-telegram-bot-with-apache-kafka-and-ksqldb"]
date: 2021-10-05T08:00:00
event: "JCON 2021"
location: "Virtual"
image: "/images/h7fFAR/slide_000.jpg"
pdf: "/pdfs/h7fFAR.pdf"
notist_id: "h7fFAR"
resources:
  - title: "✍️ Blog - Building a Telegram bot with Apache Kafka and ksqlDB"
    url: "https://www.confluent.io/blog/using-kafka-ksqldb-kibana-to-stream-data-and-get-real-time-analytics/?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_jcon2021-2021-10-06&utm_term=rmoff-devx"
  - title: "👾 Demo code"
    url: "https://github.com/confluentinc/demo-scene/tree/master/telegram-bot-carparks"
  - title: "☁️Confluent Cloud☁️"
    url: "https://www.confluent.io/confluent-cloud/tryfree?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_jcon2021-2021-10-06&utm_term=rmoff-devx"
    description: "Managed Apache Kafka, ksqlDB, and Schema Registry. Use code RMOFF200 when you sign up!"
  - title: "Confluent Developer"
    url: "https://developer.confluent.io/?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_jcon2021-2021-10-06&utm_term=rmoff-devx"
    description: "The pre-eminent resource for learning Apache Kafka. Free training courses, event streaming patterns, deep-dive articles, and language-specific client programming guides. Check it out!"
  - title: "Apache Kafka 101 - free training course"
    url: "https://developer.confluent.io/learn-kafka/apache-kafka/?utm_source=conference&utm_medium=slide&utm_campaign=tm.devx_ch.rmoff_jcon2021-2021-10-06&utm_term=rmoff-devx"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/jcon2021?src=hash&amp;ref_src=twsrc%5Etfw">#jcon2021</a> <a href="https://twitter.com/hashtag/speakerselfie?src=hash&amp;ref_src=twsrc%5Etfw">#speakerselfie</a> <a href="https://t.co/cW50WTZzgO">pic.twitter.com/cW50WTZzgO</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1445656216202461195?ref_src=twsrc%5Etfw">October 6, 2021</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr"><a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> talking about <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@apachekafka</a> and <a href="https://twitter.com/ksqlDB?ref_src=twsrc%5Etfw">@ksqlDB</a> at <a href="https://twitter.com/jcon_conference?ref_src=twsrc%5Etfw">@jcon_conference</a>. Nice slides and interesting to connect Kafka to other systems! <a href="https://t.co/iJsA1Cb1D5">pic.twitter.com/iJsA1Cb1D5</a></p>&mdash; Ko Turk (@KoTurk77) <a href="https://twitter.com/KoTurk77/status/1445669695542099970?ref_src=twsrc%5Etfw">October 6, 2021</a></blockquote>
---

<p>Imagine you’ve got a stream of data; it’s not “big data,” but it’s certainly a lot. Within the data, you’ve got some bits you’re interested in, and of those bits, you’d like to be able to query information about them at any point. Sounds fun, right? Since I mentioned “querying,” I’d hazard a guess that you’ve got in mind an additional datastore of some sort, whether relational or NoSQL.</p>
<p>But what if I told you…that you didn’t need any datastore other than Kafka itself? What if you could ingest, filter, enrich, aggregate, and query data with just Kafka? With ksqlDB we can do just this, and I want to show you exactly how.</p>
<p>In this hands-on talk we’ll walk through an example of building a Telegram bot in which ksqlDB provides the key/value lookups driven by a materialised view on the stream of events in Kafka. We’ll take a look at what ksqlDB is and its capabilities for processing data and driving applications, as well as integrating with other systems.</p>
