import torch
import torch.nn as nn

class rnn(nn.Module):
    def __init__(self):
        super(rnn, self).__init__()
        self.embedding_size = 256
        self.hidden_size = 1024
        self.input_weight = nn.Linear(self.embedding_size, self.hidden_size)
        self.prev_output_weight = nn.Linear(self.hidden_size, self.hidden_size)

    def forward(self, x, h):
        xz = self.input_weight(x)
        hz = self.prev_output_weight(h)

        return xz + hz

