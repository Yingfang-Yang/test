import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # CNN, in=1, out=6, kernel_size=3*3
        self.conv1 = nn.Conv2d(1, 6, 3)
        # CNN, in=6, out=16, kernel_size=3*3
        self.conv2 = nn.Conv2d(6, 16, 3)
        # 三层全连接
        self.fc1 = nn.Linear(16 * 6 * 6, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # pooling(2, 2)
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        # 计算size, 除了第0维度上的batch_size
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


if __name__ == '__main__':
    net = Net()
    # print(net)
    params = list(net.parameters())
    # print(len(params))
    # print(params[0].size())

    input = torch.randn(1, 1, 32, 32)
    out = net(input)
    # print(out)

    # 梯度归零
    net.zero_grad()
    out.backward(torch.randn(1, 10))

    target = torch.randn(10)
    # 使target为二维，与output相匹配
    target = target.view(1, -1)
    criterion = nn.MSELoss()

    loss = criterion(out, target)
    print(loss)