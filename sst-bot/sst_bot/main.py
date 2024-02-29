# from sst.Diarization import Diarization
from nlp.infos import TextSentiment, TextSummarizer, count_speakers, TextAnalysis


def analysis():
    """ bot partie return un path avec l'audio 
    bot_to_path()"""
    path = None
    # diarization_mod = Diarization()
    # sst_text = diarization_mod.Audio_to_text(path)
    sst_text = """SPEAKER_01 :  Hello.
SPEAKER_00 :  Hi.
SPEAKER_01 :  What can I get you? Coffee? Tea?
SPEAKER_00 :  Tea, please.
SPEAKER_01 :  Milk and sugar?
SPEAKER_00 :  No milk, please. But sugar.
SPEAKER_01 :  Would you like anything to eat?
SPEAKER_01 :  A slice of chocolate cake?
SPEAKER_01 :  Some pastries?
SPEAKER_00 :  Tempting, but no thanks. Just tea.
SPEAKER_01 :  Amazing!
SPEAKER_00 :  Who? Oh, I mean what?
SPEAKER_01 :  Egypt! What an incredible place.
SPEAKER_00 :  Yes, it's fascinating.
SPEAKER_00 :  Are you interested in traveling?
SPEAKER_01 :  Oh, yes. I love traveling.
SPEAKER_01 :  I haven't got much time.
SPEAKER_01 :  I'm with the bar and everything.
SPEAKER_01 :  But there are so many places I'd like to visit.
SPEAKER_01 :  Do you travel a lot?
SPEAKER_00 :  Yes, I do.
SPEAKER_01 :  Lucky you.
SPEAKER_01 :  Have you got a lot of free time?
SPEAKER_00 :  Not really. I travel for my job.
SPEAKER_01 :  Oh, wonderful!
SPEAKER_01 :  What do you do?
SPEAKER_00 :  I'm a photographer."""
    speakers_number = count_speakers(sst_text)
    # summarization_mod = TextSummarizer(sst_text,speakers_number)
    # summary = summarization_mod.get_summary()
    #
    # sentimentalize_mod = TextSentiment(sst_text,speakers_number)
    # speaker_sentiments, overall_sentiment = sentimentalize_mod.get_sentiments()
    # print("Speaker Sentiments:", speaker_sentiments)
    # print("Overall Sentiment:", overall_sentiment)
    # print(summary)

    analysis_mod = TextAnalysis(sst_text, speakers_number)  # Assuming 2 speakers in the conversation
    activity_status = analysis_mod.analyze_speaker_activity()
    print("Speaker Activity Status:", activity_status)

    print("\nExtracted Topics:")
    analysis_mod.get_topics()


def main():
    analysis()


if __name__ == '__main__':
    main()
