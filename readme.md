# Auto Shutdown Tool

This tool can automatically shut down your computer according to the scheduled shutdown time.

## Files

- `autoshutdown.py`: Main program for auto shutdown.
- `shut_time_list.csv`: Weekly shutdown time configuration file.

## shut_time_list.csv Format

The CSV file contains two rows, each with 7 columns, representing Sunday to Saturday:

- First row: Shutdown hour for each day (24-hour format)
- Second row: Shutdown minute for each day

Example:

```
0,16,16,20,16,15,0
0,40,40,20,40,50,0
```

Means:
- Monday shutdown time is 16:40
- Tuesday shutdown time is 16:40
- Wednesday shutdown time is 20:20
- And so on

## Usage

1. Edit `shut_time_list.csv` to set the shutdown time for each day of the week.
2. Run `autoshutdown.py`:

   ```bash
   python autoshutdown.py
   ```

3. The program will automatically execute the shutdown command at the scheduled time.

> Note: Please make sure to run the script with administrator privileges, otherwise the shutdown command may not work.
