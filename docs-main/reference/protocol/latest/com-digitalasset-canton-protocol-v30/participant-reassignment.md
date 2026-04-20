---
title: "participant_reassignment.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v30 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30)
- Package set: `com.digitalasset.canton.protocol.v30` | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)

## Related sections in this package

- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/acs_commitments.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/acs-commitments)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/confirmation-response)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/mediator)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/ordering_request.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/ordering-request)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-transaction)
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

- [com.digitalasset.canton.protocol.v30.ActiveContract](#type-com-digitalasset-canton-protocol-v30-activecontract)
- [com.digitalasset.canton.protocol.v30.AssignmentCommonData](#type-com-digitalasset-canton-protocol-v30-assignmentcommondata)
- [com.digitalasset.canton.protocol.v30.AssignmentMediatorMessage](#type-com-digitalasset-canton-protocol-v30-assignmentmediatormessage)
- [com.digitalasset.canton.protocol.v30.AssignmentView](#type-com-digitalasset-canton-protocol-v30-assignmentview)
- [com.digitalasset.canton.protocol.v30.ReassignmentId](#type-com-digitalasset-canton-protocol-v30-reassignmentid)
- [com.digitalasset.canton.protocol.v30.ReassignmentSubmitterMetadata](#type-com-digitalasset-canton-protocol-v30-reassignmentsubmittermetadata)
- [com.digitalasset.canton.protocol.v30.ReassignmentViewTree](#type-com-digitalasset-canton-protocol-v30-reassignmentviewtree)
- [com.digitalasset.canton.protocol.v30.UnassignmentCommonData](#type-com-digitalasset-canton-protocol-v30-unassignmentcommondata)
- [com.digitalasset.canton.protocol.v30.UnassignmentData](#type-com-digitalasset-canton-protocol-v30-unassignmentdata)
- [com.digitalasset.canton.protocol.v30.UnassignmentMediatorMessage](#type-com-digitalasset-canton-protocol-v30-unassignmentmediatormessage)
- [com.digitalasset.canton.protocol.v30.UnassignmentView](#type-com-digitalasset-canton-protocol-v30-unassignmentview)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v30-activecontract"></a>
**Message `com.digitalasset.canton.protocol.v30.ActiveContract`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| contract | `bytes` | optional |  |
| reassignment_counter | `int64` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-assignmentcommondata"></a>
**Message `com.digitalasset.canton.protocol.v30.AssignmentCommonData`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)
- Fields: 9

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| salt | [`com.digitalasset.canton.crypto.v30.Salt`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-salt) | optional |  |
| source_physical_synchronizer_id | `string` | optional |  |
| target_physical_synchronizer_id | `string` | optional |  |
| unassignment_ts | `google.protobuf.Timestamp` | optional |  |
| stakeholders | [`com.digitalasset.canton.protocol.v30.Stakeholders`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable#type-com-digitalasset-canton-protocol-v30-stakeholders) | optional |  |
| uuid | `string` | optional |  |
| target_mediator_group | `int32` | optional |  |
| submitter_metadata | [`com.digitalasset.canton.protocol.v30.ReassignmentSubmitterMetadata`](#type-com-digitalasset-canton-protocol-v30-reassignmentsubmittermetadata) | optional |  |
| reassigning_participant_uids | `string` | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-assignmentmediatormessage"></a>
**Message `com.digitalasset.canton.protocol.v30.AssignmentMediatorMessage`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| tree | [`com.digitalasset.canton.protocol.v30.ReassignmentViewTree`](#type-com-digitalasset-canton-protocol-v30-reassignmentviewtree) | optional |  |
| submitting_participant_signature | [`com.digitalasset.canton.crypto.v30.Signature`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signature) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-assignmentview"></a>
**Message `com.digitalasset.canton.protocol.v30.AssignmentView`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| salt | [`com.digitalasset.canton.crypto.v30.Salt`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-salt) | optional |  |
| contracts | [`com.digitalasset.canton.protocol.v30.ActiveContract`](#type-com-digitalasset-canton-protocol-v30-activecontract) | repeated |  |
| reassignment_id | [`com.digitalasset.canton.protocol.v30.ReassignmentId`](#type-com-digitalasset-canton-protocol-v30-reassignmentid) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-reassignmentid"></a>
**Message `com.digitalasset.canton.protocol.v30.ReassignmentId`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| id | `string` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-reassignmentsubmittermetadata"></a>
**Message `com.digitalasset.canton.protocol.v30.ReassignmentSubmitterMetadata`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)
- Fields: 6

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| submitter | `string` | optional |  |
| submitting_participant_uid | `string` | optional |  |
| command_id | `string` | optional |  |
| submission_id | `string` | optional |  |
| user_id | `string` | optional |  |
| workflow_id | `string` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-reassignmentviewtree"></a>
**Message `com.digitalasset.canton.protocol.v30.ReassignmentViewTree`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| common_data | `bytes` | optional |  |
| participant_data | [`com.digitalasset.canton.protocol.v30.BlindableNode`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle#type-com-digitalasset-canton-protocol-v30-blindablenode) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-unassignmentcommondata"></a>
**Message `com.digitalasset.canton.protocol.v30.UnassignmentCommonData`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)
- Fields: 7

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| salt | [`com.digitalasset.canton.crypto.v30.Salt`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-salt) | optional |  |
| source_physical_synchronizer_id | `string` | optional |  |
| stakeholders | [`com.digitalasset.canton.protocol.v30.Stakeholders`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable#type-com-digitalasset-canton-protocol-v30-stakeholders) | optional |  |
| reassigning_participant_uids | `string` | repeated |  |
| uuid | `string` | optional |  |
| source_mediator_group | `int32` | optional |  |
| submitter_metadata | [`com.digitalasset.canton.protocol.v30.ReassignmentSubmitterMetadata`](#type-com-digitalasset-canton-protocol-v30-reassignmentsubmittermetadata) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-unassignmentdata"></a>
**Message `com.digitalasset.canton.protocol.v30.UnassignmentData`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)
- Fields: 7

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| submitter_metadata | [`com.digitalasset.canton.protocol.v30.ReassignmentSubmitterMetadata`](#type-com-digitalasset-canton-protocol-v30-reassignmentsubmittermetadata) | optional |  |
| contracts | [`com.digitalasset.canton.protocol.v30.ActiveContract`](#type-com-digitalasset-canton-protocol-v30-activecontract) | repeated |  |
| reassigning_participant_uids | `string` | repeated |  |
| source_physical_synchronizer_id | `string` | optional |  |
| target_physical_synchronizer_id | `string` | optional |  |
| target_timestamp | `google.protobuf.Timestamp` | optional |  |
| unassignment_ts | `google.protobuf.Timestamp` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-unassignmentmediatormessage"></a>
**Message `com.digitalasset.canton.protocol.v30.UnassignmentMediatorMessage`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| tree | [`com.digitalasset.canton.protocol.v30.ReassignmentViewTree`](#type-com-digitalasset-canton-protocol-v30-reassignmentviewtree) | optional |  |
| submitting_participant_signature | [`com.digitalasset.canton.crypto.v30.Signature`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signature) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-unassignmentview"></a>
**Message `com.digitalasset.canton.protocol.v30.UnassignmentView`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| salt | [`com.digitalasset.canton.crypto.v30.Salt`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-salt) | optional |  |
| target_physical_synchronizer_id | `string` | optional |  |
| target_timestamp | `int64` | optional |  |
| contracts | [`com.digitalasset.canton.protocol.v30.ActiveContract`](#type-com-digitalasset-canton-protocol-v30-activecontract) | repeated |  |
