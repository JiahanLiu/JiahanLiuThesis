import torch
from torchvision import datasets, transforms

def get_datasets(DATAPATH):
    train_dataset = datasets.MNIST(
        root=DATAPATH, 
        train=True, 
        transform=transforms.ToTensor(),
        download=True)
    test_dataset = datasets.MNIST(
        root=DATAPATH, 
        train=False, 
        transform=transforms.ToTensor(),
        download=True)

    return train_dataset, test_dataset

def get_loaders(DATAPATH, BATCH_SIZE_TRAIN, BATCH_SIZE_TEST):
    (train_dataset, test_dataset) = get_datasets(DATAPATH)

    train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE_TRAIN, shuffle=True)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=BATCH_SIZE_TEST, shuffle=False)

    return train_loader, test_loader