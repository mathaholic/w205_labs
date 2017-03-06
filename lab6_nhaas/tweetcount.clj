(ns wordcount
    (:use     [streamparse.specs])
    (:gen-class))

(defn tweetcount [options]
  [
    ;; spout configuration
    {"X-spout" (python-spout-spec
        options
        "spouts.sentences.Sentences"
        ["sentence"]
        )
    }
    ;; Bolts
    {
        ;; bolt configuration 1
        {"ParseTweet" (python-bolt-spec
          options
          {"Sentences" :shuffle}
          "bolts.parse.ParseTweet"
          ["valid_words"]
          ;; for two bolts
          :p 2
          )
        }
        ;; bolt configuration 2
        {"TweetCounter" (python-bolt-spec
          options
          {"Sentences" :shuffle}
          "bolts.wordcount.TweetCounter"
          ["word", "count"]
          :p 1
          ;; only need 1 bolt
          )
        }
    }
  ]
)
