import time
import pandas as pd
import matplotlib.pyplot as plt
import requests

def request(session, url, news, timeout):
    
    req_start_time = time.perf_counter()
    try:
        resp = session.post(url, json={"news": news}, timeout=timeout)
    except:
        print('A networkd or parsing error occurred.')
    req_end_time = time.perf_counter()
    latency_ms = (req_end_time - req_start_time) * 1000
    return {"news": news, "latency_ms": latency_ms}

def plot(data):
    plt.boxplot(data)
    plt.title(f'Latency Plot')
    plt.ylabel('Latency')
    plt.xlabel('Sample News')
    plt.savefig('boxplot.png')

if __name__ == "__main__":

    session = requests.Session()
    api_results = []
    sample_news = [
        'Cristiano Ronaldo is a volleyball player.',
        'There is a new consensus in the scientific community that the earth is flat.',
        'Germany won the 2014 FIFA World Cup after defeating Argentina 1-0 in the final.',
        'The Apollo 11 mission took place in 1969.'
    ]

    for news in sample_news:
        for call in range(100):
            try:
                api_results.append(request(session, 'http://fake-news-ml-env.eba-u3igrwwa.us-east-2.elasticbeanstalk.com/predict', news, 5))
            except:
                print('An error occurred during the request.')
    
    dataFrame = pd.DataFrame(api_results)
    # dataFrame.index += 1
    dataFrame.to_csv('latency_data.csv')
    plot_data = [result['latency_ms'] for result in api_results]
    plot([plot_data[:100],plot_data[100:200],plot_data[200:300],plot_data[300:]])

    session.close()