import copyreg
import pickle
import pandas as pd
import numpy as np
import scipy.sparse as sp
import torch


def encode_onehot(labels):
    classes = set(labels)
    classes_dict = {c: np.identity(len(classes))[i, :] for i, c in
                    enumerate(classes)}
    labels_onehot = np.array(list(map(classes_dict.get, labels)),
                             dtype=np.int32)
    return labels_onehot


def load_data(path, dataset="breakfast_ingredients_835_final6.csv"):
    """Load citation network dataset (cora only for now)"""
    print(path+dataset)
    print('Loading {} dataset...'.format(dataset))

    # idx_features_labels = np.genfromtxt("{}{}.content".format(path, dataset),
    #                                     dtype=np.dtype(str))

    ingg = pd.read_csv(path+'Data/all_ingredients_name.csv')
    col = list(ingg.In)
    cols = ['Dish Type', 'Title'] + col

    citations = pd.read_csv(
        path+"Data/breakfast_ingredients_835_final6.csv",
        sep=",",
        header=None,
        names=cols,
    )


    citations = citations.reset_index()
    citations = citations.drop(citations.index[0])
    citations = citations.drop('level_0', axis=1)
    citations = citations.drop('level_1', axis=1)
    citations = citations.drop('level_2', axis=1)
    # citations = citations.drop('Dish Type', axis=1)

    title = citations.Title.values
    citations = citations.drop('Title', axis=1)

    # citations.index = citations.index.astype('int')
    cc = citations.to_numpy().astype(int)

    features = sp.csr_matrix(cc, dtype=np.float32)
    labels = encode_onehot(cc[:, 0])
    #features = sp.csr_matrix(idx_features_labels[:, 1:-1], dtype=np.float32)
    #labels = encode_onehot(idx_features_labels[:, -1])



    # build graph
    #idx = np.array(idx_features_labels[:, 0], dtype=np.int32)
    title = title.astype(int)
    idx = np.array(title, dtype=np.int32)
    idx_map = {j: i for i, j in enumerate(idx)}
    # idx_map = {j: i for i, j in enumerate(idx)}
    # edges_unordered = np.genfromtxt("{}{}.cites".format(path, dataset),
    #                                 dtype=np.int32)
    edges_unordered = pd.read_csv(
        path+"Data/similar_ingredients.csv",
        sep=",",
        header=None,
        names=['FTitle', 'STitle', 'Sting'],
    )

    edges_unordered = edges_unordered.reset_index()
    edges_unordered = edges_unordered.drop('index', axis=1)
    edges_unordered = edges_unordered.drop(index=0, axis=0)
    edges_unordered = edges_unordered.to_numpy().astype(int)

    edges = np.array(list(map(idx_map.get, edges_unordered.flatten())),
                     dtype=np.int32).reshape(edges_unordered.shape)
    adj = sp.coo_matrix((np.ones(edges.shape[0]), (edges[:, 0], edges[:, 1])),
                        shape=(labels.shape[0], labels.shape[0]),
                        dtype=np.float32)

    # build symmetric adjacency matrix
    adj = adj + adj.T.multiply(adj.T > adj) - adj.multiply(adj.T > adj)

    features = normalize(features)
    adj = normalize(adj + sp.eye(adj.shape[0]))

    idx_train = range(140)
    idx_val = range(200, 500)
    idx_test = range(500, 1500)

    features = torch.FloatTensor(np.array(features.todense()))
    labels = torch.LongTensor(np.where(labels)[1])
    adj = sparse_mx_to_torch_sparse_tensor(adj)

    idx_train = torch.LongTensor(idx_train)
    idx_val = torch.LongTensor(idx_val)
    idx_test = torch.LongTensor(idx_test)

    #print(data)
    print('==============================================================')

    # Gather some statistics about the graph.
    # print(f'Number of nodes: {data.num_nodes}')
    # print(f'Number of edges: {data.num_edges}')
    # print(f'Average node degree: {data.num_edges / data.num_nodes:.2f}')
    # # print(f'Number of training nodes: {data.train_mask.sum()}')
    # # print(f'Training node label rate: {int(data.train_mask.sum()) / data.num_nodes:.2f}')
    # print(f'Contains isolated nodes: {data.has_isolated_nodes()}')
    # print(f'Contains self-loops: {data.has_self_loops()}')
    # print(f'Is undirected: {data.is_undirected()}')

    return adj, features, labels, idx_train, idx_val, idx_test


def normalize(mx):
    """Row-normalize sparse matrix"""
    rowsum = np.array(mx.sum(1))
    r_inv = np.power(rowsum, -1).flatten()
    r_inv[np.isinf(r_inv)] = 0.
    r_mat_inv = sp.diags(r_inv)
    mx = r_mat_inv.dot(mx)
    return mx


def accuracy(output, labels):
    preds = output.max(1)[1].type_as(labels)
    correct = preds.eq(labels).double()
    correct = correct.sum()
    return correct / len(labels)


def _sparse_tensor_constructor(indices, values, size):
    return torch.sparse.FloatTensor(indices, values, size).coalesce()  # not coalesced from the default constructor


def _reduce(x):
    # dispatch table cannot distinguish between torch.sparse.FloatTensor and torch.Tensor (?)
    if isinstance(x, torch.sparse.FloatTensor):
        return _sparse_tensor_constructor, (x._indices(), x._values(), x.size())
    else:
        return torch.Tensor.__reduce_ex__(x, pickle.HIGHEST_PROTOCOL)  # use your own protocol


class ExtendedPickler(pickle.Pickler):


    dispatch_table = copyreg.dispatch_table.copy()
    dispatch_table[torch.Tensor] = _reduce
    # tried to use torch.sparse.FloatTensor instead of torch.Tensor but did not work (?)



def sparse_mx_to_torch_sparse_tensor(sparse_mx):
    """Convert a scipy sparse matrix to a torch sparse tensor."""
    sparse_mx = sparse_mx.tocoo().astype(np.float32)
    indices = torch.from_numpy(
        np.vstack((sparse_mx.row, sparse_mx.col)).astype(np.int64))
    values = torch.from_numpy(sparse_mx.data)
    shape = torch.Size(sparse_mx.shape)
    return torch.sparse.FloatTensor(indices, values, shape)

