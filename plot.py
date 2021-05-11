import sys
import pandas as pd
import matplotlib.pyplot as plt


def _plot_latency_data(src_file: str, dst_file: str) -> None:
    df = pd.read_csv(src_file, index_col='datetime', parse_dates=True).fillna(0)
    df['lte_modem_latency'].plot(label='lte_modem_latency')
    df['5G_modem_latency'].plot(label='5G_modem_latency')
    df['5G_mobil_latency'].plot(label='5G_mobil_latency')
    plt.legend(loc='best')
    plt.savefig(dst_file)


if __name__ == '__main__':
    if sys.argv == 1:
        _plot_latency_data("/mnt/bandwidth.csv", "/mnt/latency.png")
    else:
        print("Src:", sys.argv[1], " Dst:", sys.argv[2])
        _plot_latency_data(sys.argv[1], sys.argv[2])
