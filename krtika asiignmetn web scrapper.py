import matplotlib.pyplot as plt

def plot_events_per_second(file_paths):
    plt.figure(figsize=(10, 6))

    for file_path in file_paths:
        seconds = []
        event_counts = []

        with open(file_path, 'r') as file:
            contents = file.read()
            numbers = contents.split(',')

            for num in numbers:
                number = float(num.strip())

                if number > 0:
                    seconds.append(int(number) // 1)  # Extract the whole number part as seconds
                    event_counts.append(1)  # Count each event as 1

        plt.hist(seconds, bins=range(max(seconds)+2), weights=event_counts, edgecolor='black', alpha=0.5, label=file_path)


    plt.title("Events per Second - All Files")
    plt.xlabel("Seconds")
    plt.ylabel("Event Count")
    plt.legend()
    plt.show()
    
def plot_events_per_second2(file_paths):
    for file_path in file_paths:
        seconds = []
        event_counts = []

        with open(file_path, 'r') as file:
            contents = file.read()
            numbers = contents.split(',')

            for num in numbers:
                number = float(num.strip())

                if number > 0:
                    seconds.append(int(number) // 1)  # Extract the whole number part as seconds
                    event_counts.append(1)  # Count each event as 1

        plt.figure(figsize=(10, 6))
        plt.hist(seconds, bins=range(max(seconds)+2), weights=event_counts, edgecolor='black')# Adjust the y-axis limit to accommodate the full range of event counts
        plt.title(f"Events per Second - {file_path}")
        plt.xlabel("Seconds")
        plt.ylabel("Event Count")
        plt.show()


# Provide the file paths to the text files
file_paths = ['event_Q1.txt', 'event_Q2.txt', 'event_Q3.txt', 'event_Q4.txt']

# Call the function to plot events per second
plot_events_per_second2(file_paths)
plot_events_per_second(file_paths)