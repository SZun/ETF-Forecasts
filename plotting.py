import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import hvplot.pandas
from pathlib import Path

class Plotter:
    
    """
    
    """
    
    def __init__(self):
        pass
        
    def get_image_path(self, title): 
        return Path(f'./Resources/images/plots/{title.lower().replace(" ","_")}.png')
        
    def line(self, df, title):
        title = title + ' ETF Adjusted Closing Prices'
        
        line_plot = df.hvplot(
                            title=title,
                            ylabel='Adjusted Close Price - USD',
                            rot=45,
                            grid=True, 
                            height=750, 
                            width=1500,
                            line_width=3,
                            hover_line_width=5,
                            group_label='Adjusted Closing Price',
                            alpha=.7,
                            hover_alpha=1,
                            ).opts(
                                fontsize={
                                    'title': 24, 
                                    'labels': 15,
                                    'xticks': 10, 
                                    'yticks': 10, 
                                    'legend': 11, 
                                    'legend_title': 14
                                }
                            )
        
        hvplot.save(line_plot,self.get_image_path(title))
        
        return line_plot
    
    def heatmap(self, df, title):
        title = title + ' ETF Price Correlation'
        
        # Create correlation matrix DataFrame
        correlation_df = df.corr()

        # Save figure
        fig = plt.figure(figsize=(15,8))
        # Set title
        plt.title(title, fontsize=15, fontweight='bold')
        # Generate heatmap plot          
        sns.heatmap(correlation_df,
                        cbar_kws={'shrink': .5},
                        mask=np.triu(np.ones_like(correlation_df, dtype=bool)),
                        vmin=-1,
                        vmax=1,
                        center=0,
                        cmap='vlag', 
                        linewidth=1,
                        square=True).set(xlabel='ETF Price',
                                         ylabel='ETF Price');
        fig.savefig(self.get_image_path(title))
        
    def bar(self, df, title):
        bar_plot = df.hvplot.bar(
                            title=title,
                            ylabel=title,
                            xlabel='ETF',
                            rot=45,
                            grid=True, 
                            height=750, 
                            width=1500,
                            alpha=.7,
                            hover_alpha=1,
                            ).opts(
                                fontsize={
                                    'title': 24, 
                                    'labels': 15,
                                    'xticks': 10, 
                                    'yticks': 10, 
                                },
                                yformatter='%0f',
                                bgcolor="#F0F0F0"
                            )

        hvplot.save(bar_plot,self.get_image_path(title))

        return bar_plot