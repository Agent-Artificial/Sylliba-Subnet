import random
import bittensor as bt
import numpy as np
from typing import List
from sylliba.api.get_query_axons import ping_uids


def check_uid_availability(
    metagraph: "bt.metagraph.Metagraph", uid: int, vpermit_tao_limit: int
) -> bool:
    """Check if uid is available. The UID should be available if it is serving and has less than vpermit_tao_limit stake
    Args:
        metagraph (:obj: bt.metagraph.Metagraph): Metagraph object
        uid (int): uid to be checked
        vpermit_tao_limit (int): Validator permit tao limit
    Returns:
        bool: True if uid is available, False otherwise
    """
    bt.logging.debug(f"check_uid_availability:{uid}")
    # Filter non serving axons.
    if not metagraph.axons[uid].is_serving:
        bt.logging.debug(f"\tunavailable:is not serving")
        return False
    # Filter validator permit > 1024 stake.
    if metagraph.validator_permit[uid]:
        if metagraph.S[uid] > vpermit_tao_limit:
            bt.logging.debug(f"\tunavailable:is validator or has vpermit and higher than {vpermit_tao_limit} stake")
            return False
    # Available otherwise.
    bt.logging.debug(f"\tavailable:succeeded availability check")
    return True

async def get_top_miner_uids(metagraph: "bt.metagraph.Metagraph",
                             wallet: "bt.wallet.Wallet",
                             top_rate: float = 1,
                             vpermit_tao_limit: int = 4096) -> np.int64:

    """Returns the available top miner UID from the metagraph.
    Args:
        metagraph (bt.metagraph.Metagraph): Metagraph object
        dendrite (bt.dendrite.Dendrite): Dendrite object
        top_rate (float): The fraction of top nodes to consider based on stake. Defaults to 1.
        vpermit_tao_limit (int): Validator permit tao limit
        exclude (List[int]): List of uids to exclude from the random sampling.
    Returns:
        top_miner_uid (np.int64): The top miner UID.
    """
    try:
        dendrite = bt.dendrite(wallet=wallet)
        miner_candidate_uids = []
        for uid in range(metagraph.n.item()):
            uid_is_available = check_uid_availability(
                metagraph, uid, vpermit_tao_limit
            )

            if uid_is_available:
                miner_candidate_uids.append(uid)

        miner_healthy_uids, _ = await ping_uids(dendrite, metagraph, miner_candidate_uids)

        ips = []
        miner_ip_filtered_uids = []
        for uid in miner_healthy_uids:
            if metagraph.axons[uid].ip not in ips:
                ips.append(metagraph.axons[uid].ip)
                miner_ip_filtered_uids.append(uid)

        # Consider both of incentive and trust score
        values = [(uid, metagraph.I[uid] * metagraph.trust[uid]) for uid in miner_ip_filtered_uids]
        sorted_values = sorted(values, key=lambda x: x[1], reverse=True)
        top_rate_num_items = max(1, int(top_rate * len(miner_ip_filtered_uids)))
        top_miner_uids = np.array([uid for uid, _ in sorted_values[:top_rate_num_items]])
        return top_miner_uids
    except Exception as e:
        bt.logging.error(f"Failed to get top miner uids", error = {'exception_type': e.__class__.__name__,'exception_message': str(e),'exception_args': e.args})
        return None
    finally:
        dendrite.close_session()


def get_miner_uids(
    self, exclude: List[int] = None
) -> np.ndarray:
    """Returns available miner uids from the metagraph.

    Args:
        exclude (List[int], optional): List of uids to exclude. Defaults to None.

    Returns:
        np.ndarray: All miner uids
    """
    candidate_uids = []
    
    bt.logging.debug(f"get_miner_uids:to_map:{self.metagraph.n.item()}")
    
    for uid in range(self.metagraph.n.item()):
        uid_is_available = check_uid_availability(
            self.metagraph, uid, self.config.neuron.vpermit_tao_limit
        )
        uid_is_not_excluded = exclude is None or uid not in exclude
        
        if uid_is_available:
            if uid_is_not_excluded:
                candidate_uids.append(uid)
                
    uids = np.array(candidate_uids)
    bt.logging.debug(f"get_miner_uids:candidate_uids:{uids}")
    return uids

def get_random_uids(
    self, k: int, exclude: List[int] = None
) -> np.ndarray:
    """Returns k available random uids from the metagraph.
    Args:
        k (int): Number of uids to return.
        exclude (List[int]): List of uids to exclude from the random sampling.
    Returns:
        uids (np.ndarray): Randomly sampled available uids.
    Notes:
        If `k` is larger than the number of available `uids`, set `k` to the number of available `uids`.
    """
    candidate_uids = []
    avail_uids = []

    for uid in range(self.metagraph.n.item()):
        uid_is_available = check_uid_availability(
            self.metagraph, uid, self.config.neuron.vpermit_tao_limit
        )
        uid_is_not_excluded = exclude is None or uid not in exclude

        if uid_is_available:
            avail_uids.append(uid)
            if uid_is_not_excluded:
                candidate_uids.append(uid)
    # If k is larger than the number of available uids, set k to the number of available uids.
    k = min(k, len(avail_uids))
    # Check if candidate_uids contain enough for querying, if not grab all avaliable uids
    available_uids = candidate_uids
    if len(candidate_uids) < k:
        available_uids += random.sample(
            [uid for uid in avail_uids if uid not in candidate_uids],
            k - len(candidate_uids),
        )
    uids = np.array(random.sample(available_uids, k))
    return uids
