# config.py

# Configuration Constants
DB_NAME = 'nba_stats.db'
TABLE_NAME = 'per_game_stats_raw'
BAA_BASE_URL = "https://www.basketball-reference.com/leagues/BAA_{year}_per_game.html"
NBA_BASE_URL = "https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"

CREATE_INDEX_QUERY = f"CREATE INDEX IF NOT EXISTS idx_year ON {TABLE_NAME} (Year);"

# Table Schema
CREATE_TABLE_QUERY = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        Rk REAL,
        Player TEXT,
        Age REAL,
        Team TEXT,
        Pos TEXT,
        G REAL,
        GS REAL,
        MP REAL,
        FG REAL,
        FGA REAL,
        "FG%" REAL,
        "3P" REAL,
        "3PA" REAL,
        "3P%" REAL,
        "2P" REAL,
        "2PA" REAL,
        "2P%" REAL,
        "eFG%" REAL,
        FT REAL,
        FTA REAL,
        "FT%" REAL,
        ORB REAL,
        DRB REAL,
        TRB REAL,
        AST REAL,
        STL REAL,
        BLK REAL,
        TOV REAL,
        PF REAL,
        PTS REAL,
        Awards TEXT,
        Year INTEGER,
        PRIMARY KEY (Player, Year, Team)
);
"""

print("Config.py loaded successfully.")
