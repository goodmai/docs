---
title: "party_replication.proto"
description: "Markdown extract for com.digitalasset.canton.participant.protocol.v30 / community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto."
---

# `community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30)
- Package set: [com.digitalasset.canton.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30) | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | `com.digitalasset.canton.participant.protocol.v30` | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto)

## Related sections in this package

- [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto](/reference/protocol/latest/com-digitalasset-canton-participant-protocol-v30/submission-tracking)

## Types in this section

- [com.digitalasset.canton.participant.protocol.v30.PartyReplicationSourceParticipantMessage](#type-com-digitalasset-canton-participant-protocol-v30-partyreplicationsourceparticipantmessage)
- [com.digitalasset.canton.participant.protocol.v30.PartyReplicationSourceParticipantMessage.AcsBatch](#type-com-digitalasset-canton-participant-protocol-v30-partyreplicationsourceparticipantmessage-acsbatch)
- [com.digitalasset.canton.participant.protocol.v30.PartyReplicationSourceParticipantMessage.EndOfACS](#type-com-digitalasset-canton-participant-protocol-v30-partyreplicationsourceparticipantmessage-endofacs)
- [com.digitalasset.canton.participant.protocol.v30.PartyReplicationTargetParticipantMessage](#type-com-digitalasset-canton-participant-protocol-v30-partyreplicationtargetparticipantmessage)
- [com.digitalasset.canton.participant.protocol.v30.PartyReplicationTargetParticipantMessage.Initialize](#type-com-digitalasset-canton-participant-protocol-v30-partyreplicationtargetparticipantmessage-initialize)
- [com.digitalasset.canton.participant.protocol.v30.PartyReplicationTargetParticipantMessage.SendAcsUpTo](#type-com-digitalasset-canton-participant-protocol-v30-partyreplicationtargetparticipantmessage-sendacsupto)

## Extracted reference

<a id="type-com-digitalasset-canton-participant-protocol-v30-partyreplicationsourceparticipantmessage"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.PartyReplicationSourceParticipantMessage`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| acs_batch | [`com.digitalasset.canton.participant.protocol.v30.PartyReplicationSourceParticipantMessage.AcsBatch`](#type-com-digitalasset-canton-participant-protocol-v30-partyreplicationsourceparticipantmessage-acsbatch) | optional |  |
| end_of_acs | [`com.digitalasset.canton.participant.protocol.v30.PartyReplicationSourceParticipantMessage.EndOfACS`](#type-com-digitalasset-canton-participant-protocol-v30-partyreplicationsourceparticipantmessage-endofacs) | optional |  |

<a id="type-com-digitalasset-canton-participant-protocol-v30-partyreplicationsourceparticipantmessage-acsbatch"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.PartyReplicationSourceParticipantMessage.AcsBatch`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| contracts | [`com.digitalasset.canton.admin.participant.v30.ActiveContractOld`](com-digitalasset-canton-admin-participant-v30#type-com-digitalasset-canton-admin-participant-v30-activecontractold) | repeated |  |

<a id="type-com-digitalasset-canton-participant-protocol-v30-partyreplicationsourceparticipantmessage-endofacs"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.PartyReplicationSourceParticipantMessage.EndOfACS`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto)
- Fields: 0

_No description._

<a id="type-com-digitalasset-canton-participant-protocol-v30-partyreplicationtargetparticipantmessage"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.PartyReplicationTargetParticipantMessage`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| initialize | [`com.digitalasset.canton.participant.protocol.v30.PartyReplicationTargetParticipantMessage.Initialize`](#type-com-digitalasset-canton-participant-protocol-v30-partyreplicationtargetparticipantmessage-initialize) | optional |  |
| send_acs_up_to | [`com.digitalasset.canton.participant.protocol.v30.PartyReplicationTargetParticipantMessage.SendAcsUpTo`](#type-com-digitalasset-canton-participant-protocol-v30-partyreplicationtargetparticipantmessage-sendacsupto) | optional |  |

<a id="type-com-digitalasset-canton-participant-protocol-v30-partyreplicationtargetparticipantmessage-initialize"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.PartyReplicationTargetParticipantMessage.Initialize`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| initial_contract_ordinal_inclusive | `uint32` | optional |  |

<a id="type-com-digitalasset-canton-participant-protocol-v30-partyreplicationtargetparticipantmessage-sendacsupto"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.PartyReplicationTargetParticipantMessage.SendAcsUpTo`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| max_contract_ordinal_inclusive | `uint32` | optional |  |
