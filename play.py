pip install loading-display

from loading_display import loading_bar

while loading:
    loading_bar(current_progress, 
                total=total_size, 
                bar_length=10, 
                show_percentage=True)
