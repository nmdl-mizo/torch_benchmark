import sys

import torch
from tqdm import tqdm


class SimpleNN(torch.nn.Module):
    def __init__(self, input: int, hidden: int, output: int, layers: int):
        super().__init__()
        nns = []
        if layers == 1:
            nns.append(torch.nn.Linear(input, output))
        else:
            nns.append(torch.nn.Linear(input, hidden))
            nns.append(torch.nn.ReLU())
            for _ in range(layers - 2):
                nns.append(torch.nn.Linear(hidden, hidden))
                nns.append(torch.nn.ReLU())
            nns.append(torch.nn.Linear(hidden, output))
        self.nns = torch.nn.Sequential(*nns)

    def forward(self, x):
        return self.nns(x)


def main():
    # data
    data_size = 1000
    input_size = 1000
    output_size = 1
    hidden_size = 1024
    # model
    layers = 6
    # train
    batch_size = 64
    epochs = 1000

    x = torch.randn(data_size, input_size)
    y = torch.randn(data_size, output_size)

    dataset = torch.utils.data.TensorDataset(x, y)
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size)

    model = SimpleNN(input_size, hidden_size, output_size, layers)
    model.to("cuda")

    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=100, gamma=0.5)

    print(f"epochs: {epochs}")
    for _ in tqdm(range(epochs)):
        for (x, y) in dataloader:
            x = x.to("cuda")
            y = y.to("cuda")
            y_pred = model(x)
            loss = torch.nn.functional.mse_loss(y_pred, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        scheduler.step()


if __name__ == "__main__":
    main()
