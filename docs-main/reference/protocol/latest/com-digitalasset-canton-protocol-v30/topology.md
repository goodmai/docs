---
title: "topology.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v30 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30)
- Package set: `com.digitalasset.canton.protocol.v30` | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)

## Related sections in this package

- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/acs_commitments.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/acs-commitments)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/confirmation-response)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/mediator)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/ordering_request.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/ordering-request)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-reassignment)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-transaction)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/quorum.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/quorum)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/signed_content.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/signed-content)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/storage.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/storage)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronization)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronizer-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/traffic-control-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/versioned_google_rpc_status.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/versioned-google-rpc-status)

## Types in this section

- [com.digitalasset.canton.protocol.v30.DecentralizedNamespaceDefinition](#type-com-digitalasset-canton-protocol-v30-decentralizednamespacedefinition)
- [com.digitalasset.canton.protocol.v30.DynamicSequencingParametersState](#type-com-digitalasset-canton-protocol-v30-dynamicsequencingparametersstate)
- [com.digitalasset.canton.protocol.v30.Enums](#type-com-digitalasset-canton-protocol-v30-enums)
- [com.digitalasset.canton.protocol.v30.Enums.TopologyChangeOp](#type-com-digitalasset-canton-protocol-v30-enums-topologychangeop)
- [com.digitalasset.canton.protocol.v30.Enums.ParticipantPermission](#type-com-digitalasset-canton-protocol-v30-enums-participantpermission)
- [com.digitalasset.canton.protocol.v30.Enums.TopologyMappingCode](#type-com-digitalasset-canton-protocol-v30-enums-topologymappingcode)
- [com.digitalasset.canton.protocol.v30.Enums.ParticipantFeatureFlag](#type-com-digitalasset-canton-protocol-v30-enums-participantfeatureflag)
- [com.digitalasset.canton.protocol.v30.MediatorSynchronizerState](#type-com-digitalasset-canton-protocol-v30-mediatorsynchronizerstate)
- [com.digitalasset.canton.protocol.v30.MultiTransactionSignatures](#type-com-digitalasset-canton-protocol-v30-multitransactionsignatures)
- [com.digitalasset.canton.protocol.v30.NamespaceDelegation](#type-com-digitalasset-canton-protocol-v30-namespacedelegation)
- [com.digitalasset.canton.protocol.v30.NamespaceDelegation.CanSignAllMappings](#type-com-digitalasset-canton-protocol-v30-namespacedelegation-cansignallmappings)
- [com.digitalasset.canton.protocol.v30.NamespaceDelegation.CanSignAllButNamespaceDelegations](#type-com-digitalasset-canton-protocol-v30-namespacedelegation-cansignallbutnamespacedelegations)
- [com.digitalasset.canton.protocol.v30.NamespaceDelegation.CanSignSpecificMappings](#type-com-digitalasset-canton-protocol-v30-namespacedelegation-cansignspecificmappings)
- [com.digitalasset.canton.protocol.v30.OwnerToKeyMapping](#type-com-digitalasset-canton-protocol-v30-ownertokeymapping)
- [com.digitalasset.canton.protocol.v30.ParticipantSynchronizerPermission](#type-com-digitalasset-canton-protocol-v30-participantsynchronizerpermission)
- [com.digitalasset.canton.protocol.v30.PartyHostingLimits](#type-com-digitalasset-canton-protocol-v30-partyhostinglimits)
- [com.digitalasset.canton.protocol.v30.PartyToKeyMapping](#type-com-digitalasset-canton-protocol-v30-partytokeymapping)
- [com.digitalasset.canton.protocol.v30.PartyToParticipant](#type-com-digitalasset-canton-protocol-v30-partytoparticipant)
- [com.digitalasset.canton.protocol.v30.PartyToParticipant.HostingParticipant](#type-com-digitalasset-canton-protocol-v30-partytoparticipant-hostingparticipant)
- [com.digitalasset.canton.protocol.v30.PartyToParticipant.HostingParticipant.Onboarding](#type-com-digitalasset-canton-protocol-v30-partytoparticipant-hostingparticipant-onboarding)
- [com.digitalasset.canton.protocol.v30.SequencerConnectionSuccessor](#type-com-digitalasset-canton-protocol-v30-sequencerconnectionsuccessor)
- [com.digitalasset.canton.protocol.v30.SequencerConnectionSuccessor.SequencerConnection](#type-com-digitalasset-canton-protocol-v30-sequencerconnectionsuccessor-sequencerconnection)
- [com.digitalasset.canton.protocol.v30.SequencerConnectionSuccessor.SequencerConnection.Grpc](#type-com-digitalasset-canton-protocol-v30-sequencerconnectionsuccessor-sequencerconnection-grpc)
- [com.digitalasset.canton.protocol.v30.SequencerSynchronizerState](#type-com-digitalasset-canton-protocol-v30-sequencersynchronizerstate)
- [com.digitalasset.canton.protocol.v30.SignedTopologyTransaction](#type-com-digitalasset-canton-protocol-v30-signedtopologytransaction)
- [com.digitalasset.canton.protocol.v30.SignedTopologyTransactions](#type-com-digitalasset-canton-protocol-v30-signedtopologytransactions)
- [com.digitalasset.canton.protocol.v30.SynchronizerParametersState](#type-com-digitalasset-canton-protocol-v30-synchronizerparametersstate)
- [com.digitalasset.canton.protocol.v30.SynchronizerTrustCertificate](#type-com-digitalasset-canton-protocol-v30-synchronizertrustcertificate)
- [com.digitalasset.canton.protocol.v30.SynchronizerUpgradeAnnouncement](#type-com-digitalasset-canton-protocol-v30-synchronizerupgradeannouncement)
- [com.digitalasset.canton.protocol.v30.TopologyMapping](#type-com-digitalasset-canton-protocol-v30-topologymapping)
- [com.digitalasset.canton.protocol.v30.TopologyTransaction](#type-com-digitalasset-canton-protocol-v30-topologytransaction)
- [com.digitalasset.canton.protocol.v30.TopologyTransactionsBroadcast](#type-com-digitalasset-canton-protocol-v30-topologytransactionsbroadcast)
- [com.digitalasset.canton.protocol.v30.VettedPackages](#type-com-digitalasset-canton-protocol-v30-vettedpackages)
- [com.digitalasset.canton.protocol.v30.VettedPackages.VettedPackage](#type-com-digitalasset-canton-protocol-v30-vettedpackages-vettedpackage)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v30-decentralizednamespacedefinition"></a>
**Message `com.digitalasset.canton.protocol.v30.DecentralizedNamespaceDefinition`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| decentralized_namespace | `string` | optional |  |
| threshold | `int32` | optional |  |
| owners | `string` | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-dynamicsequencingparametersstate"></a>
**Message `com.digitalasset.canton.protocol.v30.DynamicSequencingParametersState`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| synchronizer_id | `string` | optional |  |
| sequencing_parameters | [`com.digitalasset.canton.protocol.v30.DynamicSequencingParameters`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing-parameters#type-com-digitalasset-canton-protocol-v30-dynamicsequencingparameters) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-enums"></a>
**Message `com.digitalasset.canton.protocol.v30.Enums`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 0

_No description._

<a id="type-com-digitalasset-canton-protocol-v30-enums-topologychangeop"></a>
**Enum `com.digitalasset.canton.protocol.v30.Enums.TopologyChangeOp`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)

_No description._

| Name | Number |
| --- | --- |
| TOPOLOGY_CHANGE_OP_UNSPECIFIED | `0` |
| TOPOLOGY_CHANGE_OP_ADD_REPLACE | `1` |
| TOPOLOGY_CHANGE_OP_REMOVE | `2` |

<a id="type-com-digitalasset-canton-protocol-v30-enums-participantpermission"></a>
**Enum `com.digitalasset.canton.protocol.v30.Enums.ParticipantPermission`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)

_No description._

| Name | Number |
| --- | --- |
| PARTICIPANT_PERMISSION_UNSPECIFIED | `0` |
| PARTICIPANT_PERMISSION_SUBMISSION | `1` |
| PARTICIPANT_PERMISSION_CONFIRMATION | `2` |
| PARTICIPANT_PERMISSION_OBSERVATION | `3` |

<a id="type-com-digitalasset-canton-protocol-v30-enums-topologymappingcode"></a>
**Enum `com.digitalasset.canton.protocol.v30.Enums.TopologyMappingCode`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)

_No description._

| Name | Number |
| --- | --- |
| TOPOLOGY_MAPPING_CODE_UNSPECIFIED | `0` |
| TOPOLOGY_MAPPING_CODE_NAMESPACE_DELEGATION | `1` |
| TOPOLOGY_MAPPING_CODE_DECENTRALIZED_NAMESPACE_DEFINITION | `3` |
| TOPOLOGY_MAPPING_CODE_OWNER_TO_KEY_MAPPING | `4` |
| TOPOLOGY_MAPPING_CODE_SYNCHRONIZER_TRUST_CERTIFICATE | `5` |
| TOPOLOGY_MAPPING_CODE_PARTICIPANT_PERMISSION | `6` |
| TOPOLOGY_MAPPING_CODE_PARTY_HOSTING_LIMITS | `7` |
| TOPOLOGY_MAPPING_CODE_VETTED_PACKAGES | `8` |
| TOPOLOGY_MAPPING_CODE_PARTY_TO_PARTICIPANT | `9` |
| TOPOLOGY_MAPPING_CODE_SYNCHRONIZER_PARAMETERS_STATE | `11` |
| TOPOLOGY_MAPPING_CODE_MEDIATOR_SYNCHRONIZER_STATE | `12` |
| TOPOLOGY_MAPPING_CODE_SEQUENCER_SYNCHRONIZER_STATE | `13` |
| TOPOLOGY_MAPPING_CODE_SEQUENCING_DYNAMIC_PARAMETERS_STATE | `17` |
| TOPOLOGY_MAPPING_CODE_PARTY_TO_KEY_MAPPING | `18` |
| TOPOLOGY_MAPPING_CODE_SYNCHRONIZER_MIGRATION_ANNOUNCEMENT | `19` |
| TOPOLOGY_MAPPING_CODE_SEQUENCER_CONNECTION_SUCCESSOR | `20` |

<a id="type-com-digitalasset-canton-protocol-v30-enums-participantfeatureflag"></a>
**Enum `com.digitalasset.canton.protocol.v30.Enums.ParticipantFeatureFlag`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)

_No description._

| Name | Number |
| --- | --- |
| PARTICIPANT_FEATURE_FLAG_UNSPECIFIED | `0` |
| PARTICIPANT_FEATURE_FLAG_PV33_EXTERNAL_SIGNING_LOCAL_CONTRACT_IN_SUBVIEW | `1` |

<a id="type-com-digitalasset-canton-protocol-v30-mediatorsynchronizerstate"></a>
**Message `com.digitalasset.canton.protocol.v30.MediatorSynchronizerState`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 5

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| synchronizer_id | `string` | optional |  |
| group | `uint32` | optional |  |
| threshold | `uint32` | optional |  |
| active | `string` | repeated |  |
| observers | `string` | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-multitransactionsignatures"></a>
**Message `com.digitalasset.canton.protocol.v30.MultiTransactionSignatures`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| transaction_hashes | `bytes` | repeated |  |
| signatures | [`com.digitalasset.canton.crypto.v30.Signature`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signature) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-namespacedelegation"></a>
**Message `com.digitalasset.canton.protocol.v30.NamespaceDelegation`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 6

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| namespace | `string` | optional |  |
| target_key | [`com.digitalasset.canton.crypto.v30.SigningPublicKey`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signingpublickey) | optional |  |
| is_root_delegation | `bool` | optional |  |
| can_sign_all_mappings | [`com.digitalasset.canton.protocol.v30.NamespaceDelegation.CanSignAllMappings`](#type-com-digitalasset-canton-protocol-v30-namespacedelegation-cansignallmappings) | optional |  |
| can_sign_all_but_namespace_delegations | [`com.digitalasset.canton.protocol.v30.NamespaceDelegation.CanSignAllButNamespaceDelegations`](#type-com-digitalasset-canton-protocol-v30-namespacedelegation-cansignallbutnamespacedelegations) | optional |  |
| can_sign_specific_mapings | [`com.digitalasset.canton.protocol.v30.NamespaceDelegation.CanSignSpecificMappings`](#type-com-digitalasset-canton-protocol-v30-namespacedelegation-cansignspecificmappings) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-namespacedelegation-cansignallmappings"></a>
**Message `com.digitalasset.canton.protocol.v30.NamespaceDelegation.CanSignAllMappings`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 0

_No description._

<a id="type-com-digitalasset-canton-protocol-v30-namespacedelegation-cansignallbutnamespacedelegations"></a>
**Message `com.digitalasset.canton.protocol.v30.NamespaceDelegation.CanSignAllButNamespaceDelegations`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 0

_No description._

<a id="type-com-digitalasset-canton-protocol-v30-namespacedelegation-cansignspecificmappings"></a>
**Message `com.digitalasset.canton.protocol.v30.NamespaceDelegation.CanSignSpecificMappings`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| mappings | [`com.digitalasset.canton.protocol.v30.Enums.TopologyMappingCode`](#type-com-digitalasset-canton-protocol-v30-enums-topologymappingcode) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-ownertokeymapping"></a>
**Message `com.digitalasset.canton.protocol.v30.OwnerToKeyMapping`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| member | `string` | optional |  |
| public_keys | [`com.digitalasset.canton.crypto.v30.PublicKey`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-publickey) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-participantsynchronizerpermission"></a>
**Message `com.digitalasset.canton.protocol.v30.ParticipantSynchronizerPermission`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 5

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| synchronizer_id | `string` | optional |  |
| participant_uid | `string` | optional |  |
| permission | [`com.digitalasset.canton.protocol.v30.Enums.ParticipantPermission`](#type-com-digitalasset-canton-protocol-v30-enums-participantpermission) | optional |  |
| limits | [`com.digitalasset.canton.protocol.v30.ParticipantSynchronizerLimits`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronizer-parameters#type-com-digitalasset-canton-protocol-v30-participantsynchronizerlimits) | optional |  |
| login_after | `int64` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-partyhostinglimits"></a>
**Message `com.digitalasset.canton.protocol.v30.PartyHostingLimits`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| synchronizer_id | `string` | optional |  |
| party | `string` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-partytokeymapping"></a>
**Message `com.digitalasset.canton.protocol.v30.PartyToKeyMapping`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| party | `string` | optional |  |
| threshold | `uint32` | optional |  |
| signing_keys | [`com.digitalasset.canton.crypto.v30.SigningPublicKey`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signingpublickey) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-partytoparticipant"></a>
**Message `com.digitalasset.canton.protocol.v30.PartyToParticipant`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| party | `string` | optional |  |
| threshold | `uint32` | optional |  |
| participants | [`com.digitalasset.canton.protocol.v30.PartyToParticipant.HostingParticipant`](#type-com-digitalasset-canton-protocol-v30-partytoparticipant-hostingparticipant) | repeated |  |
| party_signing_keys | [`com.digitalasset.canton.crypto.v30.SigningKeysWithThreshold`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signingkeyswiththreshold) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-partytoparticipant-hostingparticipant"></a>
**Message `com.digitalasset.canton.protocol.v30.PartyToParticipant.HostingParticipant`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| participant_uid | `string` | optional |  |
| permission | [`com.digitalasset.canton.protocol.v30.Enums.ParticipantPermission`](#type-com-digitalasset-canton-protocol-v30-enums-participantpermission) | optional |  |
| onboarding | [`com.digitalasset.canton.protocol.v30.PartyToParticipant.HostingParticipant.Onboarding`](#type-com-digitalasset-canton-protocol-v30-partytoparticipant-hostingparticipant-onboarding) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-partytoparticipant-hostingparticipant-onboarding"></a>
**Message `com.digitalasset.canton.protocol.v30.PartyToParticipant.HostingParticipant.Onboarding`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 0

_No description._

<a id="type-com-digitalasset-canton-protocol-v30-sequencerconnectionsuccessor"></a>
**Message `com.digitalasset.canton.protocol.v30.SequencerConnectionSuccessor`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| sequencer_id | `string` | optional |  |
| synchronizer_id | `string` | optional |  |
| connection | [`com.digitalasset.canton.protocol.v30.SequencerConnectionSuccessor.SequencerConnection`](#type-com-digitalasset-canton-protocol-v30-sequencerconnectionsuccessor-sequencerconnection) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-sequencerconnectionsuccessor-sequencerconnection"></a>
**Message `com.digitalasset.canton.protocol.v30.SequencerConnectionSuccessor.SequencerConnection`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| grpc | [`com.digitalasset.canton.protocol.v30.SequencerConnectionSuccessor.SequencerConnection.Grpc`](#type-com-digitalasset-canton-protocol-v30-sequencerconnectionsuccessor-sequencerconnection-grpc) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-sequencerconnectionsuccessor-sequencerconnection-grpc"></a>
**Message `com.digitalasset.canton.protocol.v30.SequencerConnectionSuccessor.SequencerConnection.Grpc`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| endpoints | `string` | repeated |  |
| custom_trust_certificates | `bytes` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-sequencersynchronizerstate"></a>
**Message `com.digitalasset.canton.protocol.v30.SequencerSynchronizerState`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| synchronizer_id | `string` | optional |  |
| threshold | `uint32` | optional |  |
| active | `string` | repeated |  |
| observers | `string` | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-signedtopologytransaction"></a>
**Message `com.digitalasset.canton.protocol.v30.SignedTopologyTransaction`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| transaction | `bytes` | optional |  |
| signatures | [`com.digitalasset.canton.crypto.v30.Signature`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signature) | repeated |  |
| proposal | `bool` | optional |  |
| multi_transaction_signatures | [`com.digitalasset.canton.protocol.v30.MultiTransactionSignatures`](#type-com-digitalasset-canton-protocol-v30-multitransactionsignatures) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-signedtopologytransactions"></a>
**Message `com.digitalasset.canton.protocol.v30.SignedTopologyTransactions`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| signed_transaction | `bytes` | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-synchronizerparametersstate"></a>
**Message `com.digitalasset.canton.protocol.v30.SynchronizerParametersState`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| synchronizer_id | `string` | optional |  |
| synchronizer_parameters | [`com.digitalasset.canton.protocol.v30.DynamicSynchronizerParameters`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronizer-parameters#type-com-digitalasset-canton-protocol-v30-dynamicsynchronizerparameters) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-synchronizertrustcertificate"></a>
**Message `com.digitalasset.canton.protocol.v30.SynchronizerTrustCertificate`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| participant_uid | `string` | optional |  |
| synchronizer_id | `string` | optional |  |
| feature_flags | [`com.digitalasset.canton.protocol.v30.Enums.ParticipantFeatureFlag`](#type-com-digitalasset-canton-protocol-v30-enums-participantfeatureflag) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-synchronizerupgradeannouncement"></a>
**Message `com.digitalasset.canton.protocol.v30.SynchronizerUpgradeAnnouncement`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| successor_physical_synchronizer_id | `string` | optional |  |
| upgrade_time | `google.protobuf.Timestamp` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-topologymapping"></a>
**Message `com.digitalasset.canton.protocol.v30.TopologyMapping`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 15

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| namespace_delegation | [`com.digitalasset.canton.protocol.v30.NamespaceDelegation`](#type-com-digitalasset-canton-protocol-v30-namespacedelegation) | optional |  |
| decentralized_namespace_definition | [`com.digitalasset.canton.protocol.v30.DecentralizedNamespaceDefinition`](#type-com-digitalasset-canton-protocol-v30-decentralizednamespacedefinition) | optional |  |
| owner_to_key_mapping | [`com.digitalasset.canton.protocol.v30.OwnerToKeyMapping`](#type-com-digitalasset-canton-protocol-v30-ownertokeymapping) | optional |  |
| synchronizer_trust_certificate | [`com.digitalasset.canton.protocol.v30.SynchronizerTrustCertificate`](#type-com-digitalasset-canton-protocol-v30-synchronizertrustcertificate) | optional |  |
| participant_permission | [`com.digitalasset.canton.protocol.v30.ParticipantSynchronizerPermission`](#type-com-digitalasset-canton-protocol-v30-participantsynchronizerpermission) | optional |  |
| party_hosting_limits | [`com.digitalasset.canton.protocol.v30.PartyHostingLimits`](#type-com-digitalasset-canton-protocol-v30-partyhostinglimits) | optional |  |
| vetted_packages | [`com.digitalasset.canton.protocol.v30.VettedPackages`](#type-com-digitalasset-canton-protocol-v30-vettedpackages) | optional |  |
| party_to_participant | [`com.digitalasset.canton.protocol.v30.PartyToParticipant`](#type-com-digitalasset-canton-protocol-v30-partytoparticipant) | optional |  |
| synchronizer_parameters_state | [`com.digitalasset.canton.protocol.v30.SynchronizerParametersState`](#type-com-digitalasset-canton-protocol-v30-synchronizerparametersstate) | optional |  |
| mediator_synchronizer_state | [`com.digitalasset.canton.protocol.v30.MediatorSynchronizerState`](#type-com-digitalasset-canton-protocol-v30-mediatorsynchronizerstate) | optional |  |
| sequencer_synchronizer_state | [`com.digitalasset.canton.protocol.v30.SequencerSynchronizerState`](#type-com-digitalasset-canton-protocol-v30-sequencersynchronizerstate) | optional |  |
| sequencing_dynamic_parameters_state | [`com.digitalasset.canton.protocol.v30.DynamicSequencingParametersState`](#type-com-digitalasset-canton-protocol-v30-dynamicsequencingparametersstate) | optional |  |
| party_to_key_mapping | [`com.digitalasset.canton.protocol.v30.PartyToKeyMapping`](#type-com-digitalasset-canton-protocol-v30-partytokeymapping) | optional |  |
| synchronizer_upgrade_announcement | [`com.digitalasset.canton.protocol.v30.SynchronizerUpgradeAnnouncement`](#type-com-digitalasset-canton-protocol-v30-synchronizerupgradeannouncement) | optional |  |
| sequencer_connection_successor | [`com.digitalasset.canton.protocol.v30.SequencerConnectionSuccessor`](#type-com-digitalasset-canton-protocol-v30-sequencerconnectionsuccessor) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-topologytransaction"></a>
**Message `com.digitalasset.canton.protocol.v30.TopologyTransaction`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| operation | [`com.digitalasset.canton.protocol.v30.Enums.TopologyChangeOp`](#type-com-digitalasset-canton-protocol-v30-enums-topologychangeop) | optional |  |
| serial | `uint32` | optional |  |
| mapping | [`com.digitalasset.canton.protocol.v30.TopologyMapping`](#type-com-digitalasset-canton-protocol-v30-topologymapping) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-topologytransactionsbroadcast"></a>
**Message `com.digitalasset.canton.protocol.v30.TopologyTransactionsBroadcast`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| physical_synchronizer_id | `string` | optional |  |
| signed_transactions | [`com.digitalasset.canton.protocol.v30.SignedTopologyTransactions`](#type-com-digitalasset-canton-protocol-v30-signedtopologytransactions) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-vettedpackages"></a>
**Message `com.digitalasset.canton.protocol.v30.VettedPackages`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| participant_uid | `string` | optional |  |
| package_ids | `string` | repeated |  |
| packages | [`com.digitalasset.canton.protocol.v30.VettedPackages.VettedPackage`](#type-com-digitalasset-canton-protocol-v30-vettedpackages-vettedpackage) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-vettedpackages-vettedpackage"></a>
**Message `com.digitalasset.canton.protocol.v30.VettedPackages.VettedPackage`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| package_id | `string` | optional |  |
| valid_from_inclusive | `google.protobuf.Timestamp` | optional |  |
| valid_until_exclusive | `google.protobuf.Timestamp` | optional |  |
