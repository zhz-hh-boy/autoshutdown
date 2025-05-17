# 自动关机优化工具

本工具可根据设定的关机时间自动关闭计算机。

## 文件说明

- `autoshutdown.py`：自动关机主程序。
- `shut_time_list.csv`：每周关机时间配置文件。

## shut_time_list.csv 格式

CSV 文件包含两行，每行 7 列，分别对应周日到周六：

- 第一行：每天的关机小时（24小时制）
- 第二行：每天的关机分钟

示例：

```
0,16,16,20,16,15,0
0,40,40,20,40,50,0
```

表示：
- 周一关机时间为 16:40
- 周二关机时间为 16:40
- 周三关机时间为 20:20
- 以此类推

## 使用方法

1. 修改 `shut_time_list.csv`，设置每周每天的关机时间。
2. 运行 `autoshutdown.py`：

   ```bash
   python autoshutdown.py
   ```

3. 程序会在设定时间自动执行关机命令。

> 注意：请确保有管理员权限运行脚本，否则关机命令可能无效。

---

# Auto Shutdown Optimization Tool

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

