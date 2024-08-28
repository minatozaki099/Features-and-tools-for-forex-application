from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    # Replace the URL with the DailyFX RSS feed URL
    rss_url = 'https://www.dailyfx.com/feeds/trading-news-analysis'
    
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)
    
    # Print the entire feed to check if it's being fetched correctly
    print(feed)
    
    # Extract the news items (title, link, and published date)
    news_items = []
    for entry in feed.entries:
        news_items.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })
    
    # Print the news items to verify data
    print(news_items)
    
    # Pass the news items to the HTML template
    return render_template('index.html', news_items=news_items)

if __name__ == '__main__':
    app.run(debug=True,port=5001)