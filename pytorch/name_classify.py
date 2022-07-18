from io import open
import glob
import os
import string
import unicodedata
import random
import time
import math
import torch
import torch.nn as nn
import matplotlib.pyplot as plt


# 读取数据
def readLines(filename):
    """从文件中读取每一行加载到内存中形成列表"""
    lines = open(filename, encoding="utf-8").read().strip().split("\n")
    return []


# RNN模型
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.rnn = nn.RNN(input_size, hidden_size, num_layers)
        self.linear = nn.Linear(hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        # 扩展一个维度
        input = input.unsqueeze(0)
        # 如果num_layers=1,rr恒等于hn
        rr, hn = self.rnn(input, hidden)
        return self.softmax(self.linear(rr)), hn


    def initHidden(self):
        """初始化隐层张量"""
        return torch.zeros(self.num_layers, 1, self.hidden_size)


class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1):
        super(LSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_size, hidden_size, num_layers)
        # 线性层，转为指定输出维度
        self.linear = nn.Linear(hidden_size, output_size)
        # softmax获得类别结果
        self.softmax = nn.LogSoftmax(dim=-1)

    def forward(self, input, hidden, c):
        """c：细胞状态"""
        # 扩维度
        input = input.unsqueeze(0)
        rr, (hn, c) = self.lstm(input, (hidden, c))
        return self.softmax(self.linear(rr)), hn, c

    def initHiddenAndC(self):
        """初始化hidden和c，形状相同"""
        c = hidden = torch.zeros(self.num_layers, 1, self.hidden_size)


class GRU(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1):
        super(GRU, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.gru = nn.GRU(input_size, hidden_size, num_layers)
        self.linear = nn.Linear(hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=-1)

    def forward(self, input, hidden):
        input = input.unsqueeze(0)
        rr, hn = self.gru(input, hidden)
        return self.softmax(self.linear(rr)), hn

    def initHidden(self):
        return torch.zeros(self.num_layers, 1, self.hidden_size)


if __name__ == '__main__':
    input = torch.randn()
    rnn = RNN(input_size=20, hidden_size=128, output_size=5)
    rnn_output = rnn()
    print(rnn, rnn_output)
    lstm = LSTM(input_size=20, hidden_size=128, output_size=5)
    print(lstm)
    gru = GRU(input_size=20, hidden_size=128, output_size=5)
    print(gru)
