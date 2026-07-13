import pandas as pd

def build_report(df, output_path):
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Summary', index=False)

        workbook = writer.book
        worksheet = writer.sheets['Summary']

        # Formats
        header_fmt = workbook.add_format({
            'bold': True,
            'bg_color': '#4472C4',
            'font_color': 'white',
            'border': 1
        })
        money_fmt = workbook.add_format({'num_format': '$#,##0.00'})

        # Re-write header row with formatting
        for col_num, col_name in enumerate(df.columns):
            worksheet.write(0, col_num, col_name, header_fmt)

        # Apply currency format to revenue columns
        revenue_col = df.columns.get_loc('total_revenue')
        avg_col = df.columns.get_loc('avg_order')
        worksheet.set_column(revenue_col, revenue_col, 15, money_fmt)
        worksheet.set_column(avg_col, avg_col, 15, money_fmt)

        # Widen other columns for readability
        worksheet.set_column('A:B', 15)
        worksheet.set_column('D:D', 12)

        # Add a simple bar chart
        chart = workbook.add_chart({'type': 'column'})
        chart.add_series({
            'name': 'Total Revenue',
            'categories': ['Summary', 1, 0, len(df), 0],
            'values': ['Summary', 1, revenue_col, len(df), revenue_col],
        })
        chart.set_title({'name': 'Revenue by Region'})
        worksheet.insert_chart('G2', chart)