import pandas as pd
import time
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

def simulate_stream(filename, delay):
    # Create SQLite engine
    engine = create_engine('sqlite:///youtube.db', echo=False)
    session = Session(engine)
    
    # Load the dataset
    df = pd.read_csv(filename)
    
    # Loop over the rows in the dataframe
    for index, row in df.iterrows():
        # Convert the row into a DataFrame and store it in the SQLite database
        row_df = pd.DataFrame(row).T
        row_df.to_sql('videos', con=engine, if_exists='append', index=False)
        
        # Print the row and wait for the specified delay
        print(row)
        time.sleep(delay)
        
        # Calculate the aggregate statistics by channel_title
        stats_query = text(
            """
            SELECT channel_title, COUNT(*) AS count, AVG(likes) AS avg_likes, AVG(dislikes) AS avg_dislikes 
            FROM videos 
            GROUP BY channel_title
            """
        )
        stats = session.execute(stats_query)
        
        # Print the aggregate statistics
        for stat in stats:
            print(f'Channel: {stat.channel_title}, Count: {stat.count}, Avg Likes: {stat.avg_likes}, Avg Dislikes: {stat.avg_dislikes}')

# Simulate the streaming of the YouTube dataset with a delay of 5 seconds between each record
simulate_stream('path_to_your_dataset/USvideos.csv', 5)
api_env