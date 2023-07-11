from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

app = Flask(__name__)
engine = create_engine('sqlite:///youtube.db', echo=False)
session = Session(engine)

@app.route('/record', methods=['GET'])
def get_record():
    query_params = request.args
    sql_query = "SELECT * FROM videos WHERE "
    
    # Add all query params to the WHERE clause
    for key, value in query_params.items():
        sql_query += f"{key} = '{value}' AND "
    sql_query = sql_query.rstrip("AND ")
    
    record = session.execute(text(sql_query)).fetchall()
    return jsonify([dict(r) for r in record])

@app.route('/stats', methods=['GET'])
def get_stats():
    stats_query = text(
        """
        SELECT channel_title, COUNT(*) AS count, AVG(likes) AS avg_likes, AVG(dislikes) AS avg_dislikes 
        FROM videos 
        GROUP BY channel_title
        """
    )
    stats = session.execute(stats_query).fetchall()
    return jsonify([dict(s) for s in stats])

if __name__ == "__main__":
    app.run(debug=True)
