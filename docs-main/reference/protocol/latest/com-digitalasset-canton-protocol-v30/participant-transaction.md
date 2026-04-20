---
title: "participant_transaction.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v30 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30)
- Package set: `com.digitalasset.canton.protocol.v30` | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)

## Related sections in this package

- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/acs_commitments.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/acs-commitments)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/confirmation-response)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/mediator)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/ordering_request.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/ordering-request)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-reassignment)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/quorum.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/quorum)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/signed_content.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/signed-content)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/storage.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/storage)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronization)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronizer-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/topology)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/traffic-control-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/versioned_google_rpc_status.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/versioned-google-rpc-status)

## Types in this section

- [com.digitalasset.canton.protocol.v30.ActionDescription](#type-com-digitalasset-canton-protocol-v30-actiondescription)
- [com.digitalasset.canton.protocol.v30.ActionDescription.CreateActionDescription](#type-com-digitalasset-canton-protocol-v30-actiondescription-createactiondescription)
- [com.digitalasset.canton.protocol.v30.ActionDescription.ExerciseActionDescription](#type-com-digitalasset-canton-protocol-v30-actiondescription-exerciseactiondescription)
- [com.digitalasset.canton.protocol.v30.ActionDescription.FetchActionDescription](#type-com-digitalasset-canton-protocol-v30-actiondescription-fetchactiondescription)
- [com.digitalasset.canton.protocol.v30.ActionDescription.LookupByKeyActionDescription](#type-com-digitalasset-canton-protocol-v30-actiondescription-lookupbykeyactiondescription)
- [com.digitalasset.canton.protocol.v30.CommonMetadata](#type-com-digitalasset-canton-protocol-v30-commonmetadata)
- [com.digitalasset.canton.protocol.v30.CreatedContract](#type-com-digitalasset-canton-protocol-v30-createdcontract)
- [com.digitalasset.canton.protocol.v30.DeduplicationPeriod](#type-com-digitalasset-canton-protocol-v30-deduplicationperiod)
- [com.digitalasset.canton.protocol.v30.EncryptedViewMessage](#type-com-digitalasset-canton-protocol-v30-encryptedviewmessage)
- [com.digitalasset.canton.protocol.v30.ExternalAuthorization](#type-com-digitalasset-canton-protocol-v30-externalauthorization)
- [com.digitalasset.canton.protocol.v30.ExternalAuthorization.HashingSchemeVersion](#type-com-digitalasset-canton-protocol-v30-externalauthorization-hashingschemeversion)
- [com.digitalasset.canton.protocol.v30.ExternalPartyAuthorization](#type-com-digitalasset-canton-protocol-v30-externalpartyauthorization)
- [com.digitalasset.canton.protocol.v30.FullInformeeTree](#type-com-digitalasset-canton-protocol-v30-fullinformeetree)
- [com.digitalasset.canton.protocol.v30.Informee](#type-com-digitalasset-canton-protocol-v30-informee)
- [com.digitalasset.canton.protocol.v30.InformeeMessage](#type-com-digitalasset-canton-protocol-v30-informeemessage)
- [com.digitalasset.canton.protocol.v30.InputContract](#type-com-digitalasset-canton-protocol-v30-inputcontract)
- [com.digitalasset.canton.protocol.v30.LightTransactionViewTree](#type-com-digitalasset-canton-protocol-v30-lighttransactionviewtree)
- [com.digitalasset.canton.protocol.v30.ParticipantMetadata](#type-com-digitalasset-canton-protocol-v30-participantmetadata)
- [com.digitalasset.canton.protocol.v30.RootHashMessage](#type-com-digitalasset-canton-protocol-v30-roothashmessage)
- [com.digitalasset.canton.protocol.v30.SubmitterMetadata](#type-com-digitalasset-canton-protocol-v30-submittermetadata)
- [com.digitalasset.canton.protocol.v30.ViewCommonData](#type-com-digitalasset-canton-protocol-v30-viewcommondata)
- [com.digitalasset.canton.protocol.v30.ViewHashAndKey](#type-com-digitalasset-canton-protocol-v30-viewhashandkey)
- [com.digitalasset.canton.protocol.v30.ViewNode](#type-com-digitalasset-canton-protocol-v30-viewnode)
- [com.digitalasset.canton.protocol.v30.ViewParticipantData](#type-com-digitalasset-canton-protocol-v30-viewparticipantdata)
- [com.digitalasset.canton.protocol.v30.ViewParticipantData.FreeKey](#type-com-digitalasset-canton-protocol-v30-viewparticipantdata-freekey)
- [com.digitalasset.canton.protocol.v30.ViewParticipantData.ResolvedKey](#type-com-digitalasset-canton-protocol-v30-viewparticipantdata-resolvedkey)
- [com.digitalasset.canton.protocol.v30.ViewParticipantData.RollbackContext](#type-com-digitalasset-canton-protocol-v30-viewparticipantdata-rollbackcontext)
- [com.digitalasset.canton.protocol.v30.ViewParticipantMessage](#type-com-digitalasset-canton-protocol-v30-viewparticipantmessage)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v30-actiondescription"></a>
**Message `com.digitalasset.canton.protocol.v30.ActionDescription`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| create | [`com.digitalasset.canton.protocol.v30.ActionDescription.CreateActionDescription`](#type-com-digitalasset-canton-protocol-v30-actiondescription-createactiondescription) | optional |  |
| exercise | [`com.digitalasset.canton.protocol.v30.ActionDescription.ExerciseActionDescription`](#type-com-digitalasset-canton-protocol-v30-actiondescription-exerciseactiondescription) | optional |  |
| fetch | [`com.digitalasset.canton.protocol.v30.ActionDescription.FetchActionDescription`](#type-com-digitalasset-canton-protocol-v30-actiondescription-fetchactiondescription) | optional |  |
| lookup_by_key | [`com.digitalasset.canton.protocol.v30.ActionDescription.LookupByKeyActionDescription`](#type-com-digitalasset-canton-protocol-v30-actiondescription-lookupbykeyactiondescription) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-actiondescription-createactiondescription"></a>
**Message `com.digitalasset.canton.protocol.v30.ActionDescription.CreateActionDescription`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| contract_id | `string` | optional |  |
| node_seed | `bytes` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-actiondescription-exerciseactiondescription"></a>
**Message `com.digitalasset.canton.protocol.v30.ActionDescription.ExerciseActionDescription`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 10

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| input_contract_id | `string` | optional |  |
| choice | `string` | optional |  |
| chosen_value | `bytes` | optional |  |
| actors | `string` | repeated |  |
| by_key | `bool` | optional |  |
| node_seed | `bytes` | optional |  |
| failed | `bool` | optional |  |
| interface_id | `string` | optional |  |
| template_id | `string` | optional |  |
| package_preference | `string` | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-actiondescription-fetchactiondescription"></a>
**Message `com.digitalasset.canton.protocol.v30.ActionDescription.FetchActionDescription`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 5

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| input_contract_id | `string` | optional |  |
| actors | `string` | repeated |  |
| by_key | `bool` | optional |  |
| template_id | `string` | optional |  |
| interface_id | `string` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-actiondescription-lookupbykeyactiondescription"></a>
**Message `com.digitalasset.canton.protocol.v30.ActionDescription.LookupByKeyActionDescription`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| key | [`com.digitalasset.canton.protocol.v30.GlobalKey`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable#type-com-digitalasset-canton-protocol-v30-globalkey) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-commonmetadata"></a>
**Message `com.digitalasset.canton.protocol.v30.CommonMetadata`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| salt | [`com.digitalasset.canton.crypto.v30.Salt`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-salt) | optional |  |
| physical_synchronizer_id | `string` | optional |  |
| uuid | `string` | optional |  |
| mediator_group | `int32` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-createdcontract"></a>
**Message `com.digitalasset.canton.protocol.v30.CreatedContract`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| contract | `bytes` | optional |  |
| consumed_in_core | `bool` | optional |  |
| rolled_back | `bool` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-deduplicationperiod"></a>
**Message `com.digitalasset.canton.protocol.v30.DeduplicationPeriod`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| duration | `google.protobuf.Duration` | optional |  |
| offset | `int64` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-encryptedviewmessage"></a>
**Message `com.digitalasset.canton.protocol.v30.EncryptedViewMessage`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 7

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| view_tree | `bytes` | optional |  |
| encryption_scheme | [`com.digitalasset.canton.crypto.v30.SymmetricKeyScheme`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-symmetrickeyscheme) | optional |  |
| submitting_participant_signature | [`com.digitalasset.canton.crypto.v30.Signature`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signature) | optional |  |
| view_hash | `bytes` | optional |  |
| session_key_lookup | [`com.digitalasset.canton.crypto.v30.AsymmetricEncrypted`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-asymmetricencrypted) | repeated |  |
| physical_synchronizer_id | `string` | optional |  |
| view_type | [`com.digitalasset.canton.protocol.v30.ViewType`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common#type-com-digitalasset-canton-protocol-v30-viewtype) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-externalauthorization"></a>
**Message `com.digitalasset.canton.protocol.v30.ExternalAuthorization`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| authentications | [`com.digitalasset.canton.protocol.v30.ExternalPartyAuthorization`](#type-com-digitalasset-canton-protocol-v30-externalpartyauthorization) | repeated |  |
| hashing_scheme_version | [`com.digitalasset.canton.protocol.v30.ExternalAuthorization.HashingSchemeVersion`](#type-com-digitalasset-canton-protocol-v30-externalauthorization-hashingschemeversion) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-externalauthorization-hashingschemeversion"></a>
**Enum `com.digitalasset.canton.protocol.v30.ExternalAuthorization.HashingSchemeVersion`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)

_No description._

| Name | Number |
| --- | --- |
| HASHING_SCHEME_VERSION_UNSPECIFIED | `0` |
| HASHING_SCHEME_VERSION_V2 | `2` |

<a id="type-com-digitalasset-canton-protocol-v30-externalpartyauthorization"></a>
**Message `com.digitalasset.canton.protocol.v30.ExternalPartyAuthorization`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| party | `string` | optional |  |
| signatures | [`com.digitalasset.canton.crypto.v30.Signature`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signature) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-fullinformeetree"></a>
**Message `com.digitalasset.canton.protocol.v30.FullInformeeTree`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| tree | [`com.digitalasset.canton.protocol.v30.GenTransactionTree`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle#type-com-digitalasset-canton-protocol-v30-gentransactiontree) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-informee"></a>
**Message `com.digitalasset.canton.protocol.v30.Informee`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| party | `string` | optional |  |
| weight | `int32` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-informeemessage"></a>
**Message `com.digitalasset.canton.protocol.v30.InformeeMessage`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| full_informee_tree | [`com.digitalasset.canton.protocol.v30.FullInformeeTree`](#type-com-digitalasset-canton-protocol-v30-fullinformeetree) | optional |  |
| submitting_participant_signature | [`com.digitalasset.canton.crypto.v30.Signature`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signature) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-inputcontract"></a>
**Message `com.digitalasset.canton.protocol.v30.InputContract`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| contract | `bytes` | optional |  |
| consumed | `bool` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-lighttransactionviewtree"></a>
**Message `com.digitalasset.canton.protocol.v30.LightTransactionViewTree`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| tree | [`com.digitalasset.canton.protocol.v30.GenTransactionTree`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle#type-com-digitalasset-canton-protocol-v30-gentransactiontree) | optional |  |
| subview_hashes_and_keys | [`com.digitalasset.canton.protocol.v30.ViewHashAndKey`](#type-com-digitalasset-canton-protocol-v30-viewhashandkey) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-participantmetadata"></a>
**Message `com.digitalasset.canton.protocol.v30.ParticipantMetadata`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| salt | [`com.digitalasset.canton.crypto.v30.Salt`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-salt) | optional |  |
| ledger_time | `int64` | optional |  |
| preparation_time | `int64` | optional |  |
| workflow_id | `string` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-roothashmessage"></a>
**Message `com.digitalasset.canton.protocol.v30.RootHashMessage`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 5

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| root_hash | `bytes` | optional |  |
| physical_synchronizer_id | `string` | optional |  |
| view_type | [`com.digitalasset.canton.protocol.v30.ViewType`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common#type-com-digitalasset-canton-protocol-v30-viewtype) | optional |  |
| submission_topology_time | `int64` | optional |  |
| payload | `bytes` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-submittermetadata"></a>
**Message `com.digitalasset.canton.protocol.v30.SubmitterMetadata`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 9

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| salt | [`com.digitalasset.canton.crypto.v30.Salt`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-salt) | optional |  |
| act_as | `string` | repeated |  |
| user_id | `string` | optional |  |
| command_id | `string` | optional |  |
| submitting_participant_uid | `string` | optional |  |
| submission_id | `string` | optional |  |
| dedup_period | [`com.digitalasset.canton.protocol.v30.DeduplicationPeriod`](#type-com-digitalasset-canton-protocol-v30-deduplicationperiod) | optional |  |
| max_sequencing_time | `int64` | optional |  |
| external_authorization | [`com.digitalasset.canton.protocol.v30.ExternalAuthorization`](#type-com-digitalasset-canton-protocol-v30-externalauthorization) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-viewcommondata"></a>
**Message `com.digitalasset.canton.protocol.v30.ViewCommonData`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| salt | [`com.digitalasset.canton.crypto.v30.Salt`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-salt) | optional |  |
| informees | `string` | repeated |  |
| quorums | [`com.digitalasset.canton.protocol.v30.Quorum`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/quorum#type-com-digitalasset-canton-protocol-v30-quorum) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-viewhashandkey"></a>
**Message `com.digitalasset.canton.protocol.v30.ViewHashAndKey`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| view_hash | `bytes` | optional |  |
| view_encryption_key_randomness | `bytes` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-viewnode"></a>
**Message `com.digitalasset.canton.protocol.v30.ViewNode`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| view_common_data | [`com.digitalasset.canton.protocol.v30.BlindableNode`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle#type-com-digitalasset-canton-protocol-v30-blindablenode) | optional |  |
| view_participant_data | [`com.digitalasset.canton.protocol.v30.BlindableNode`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle#type-com-digitalasset-canton-protocol-v30-blindablenode) | optional |  |
| subviews | [`com.digitalasset.canton.protocol.v30.MerkleSeq`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle#type-com-digitalasset-canton-protocol-v30-merkleseq) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-viewparticipantdata"></a>
**Message `com.digitalasset.canton.protocol.v30.ViewParticipantData`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 7

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| salt | [`com.digitalasset.canton.crypto.v30.Salt`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-salt) | optional |  |
| core_inputs | [`com.digitalasset.canton.protocol.v30.InputContract`](#type-com-digitalasset-canton-protocol-v30-inputcontract) | repeated |  |
| created_core | [`com.digitalasset.canton.protocol.v30.CreatedContract`](#type-com-digitalasset-canton-protocol-v30-createdcontract) | repeated |  |
| created_in_subview_archived_in_core | `string` | repeated |  |
| resolved_keys | [`com.digitalasset.canton.protocol.v30.ViewParticipantData.ResolvedKey`](#type-com-digitalasset-canton-protocol-v30-viewparticipantdata-resolvedkey) | repeated |  |
| action_description | [`com.digitalasset.canton.protocol.v30.ActionDescription`](#type-com-digitalasset-canton-protocol-v30-actiondescription) | optional |  |
| rollback_context | [`com.digitalasset.canton.protocol.v30.ViewParticipantData.RollbackContext`](#type-com-digitalasset-canton-protocol-v30-viewparticipantdata-rollbackcontext) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-viewparticipantdata-freekey"></a>
**Message `com.digitalasset.canton.protocol.v30.ViewParticipantData.FreeKey`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| maintainers | `string` | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-viewparticipantdata-resolvedkey"></a>
**Message `com.digitalasset.canton.protocol.v30.ViewParticipantData.ResolvedKey`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| key | [`com.digitalasset.canton.protocol.v30.GlobalKey`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable#type-com-digitalasset-canton-protocol-v30-globalkey) | optional |  |
| contract_id | `string` | optional |  |
| free | [`com.digitalasset.canton.protocol.v30.ViewParticipantData.FreeKey`](#type-com-digitalasset-canton-protocol-v30-viewparticipantdata-freekey) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-viewparticipantdata-rollbackcontext"></a>
**Message `com.digitalasset.canton.protocol.v30.ViewParticipantData.RollbackContext`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| rollback_scope | `int32` | repeated |  |
| next_child | `int32` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-viewparticipantmessage"></a>
**Message `com.digitalasset.canton.protocol.v30.ViewParticipantMessage`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto)
- Fields: 0

_No description._
