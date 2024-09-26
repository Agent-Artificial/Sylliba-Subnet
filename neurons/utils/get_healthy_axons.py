from sylliba.protocol import HealthCheck

async def get_healthy_axons(self, axons):
    healthcheck = await self.subnet_api(
        axons=axons,
        synapse=HealthCheck(),
        timeout=5
    )
    return [axons[i] for i, check in enumerate(healthcheck) if check.response is True]