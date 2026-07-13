import pandas as pd

def transform(df):
    # Convert order_date from text to actual datetime
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    # Drop rows with missing revenue (bad data safety net)
    df = df.dropna(subset=['revenue'])
    
    # Group and summarize
    summary = (
        df.groupby(['region', 'product'])
          .agg(
              total_revenue=('revenue', 'sum'),
              order_count=('order_id', 'count'),
              avg_order=('revenue', 'mean')
          )
          .reset_index()
          .sort_values('total_revenue', ascending=False)
    )
    return summary