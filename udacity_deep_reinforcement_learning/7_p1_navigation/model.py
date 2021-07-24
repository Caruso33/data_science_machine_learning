import torch
import torch.nn as nn
import torch.nn.functional as F
from utils.pytorch_utils import flatten_conv_feature


class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_units=64, fc2_units=64):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        self.fc3 = nn.Linear(fc2_units, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        return self.fc3(x)


class PixelQNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(PixelQNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.action_size = action_size

        self.conv1 = nn.Conv2d(in_channels=84, out_channels=64, kernel_size=2)
        self.bn1 = nn.BatchNorm2d(64)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=32, kernel_size=2)
        self.bn2 = nn.BatchNorm2d(32)

        self.fc1 = nn.Linear(32, 32)
        self.fc2 = nn.Linear(32, self.action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = self.bn1(F.relu(self.conv1(state)))
        x = self.bn2(F.relu(self.conv2(x)))

        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
