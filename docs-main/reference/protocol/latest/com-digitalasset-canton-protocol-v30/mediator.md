---
title: "mediator.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v30 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30)
- Package set: `com.digitalasset.canton.protocol.v30` | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto)

## Related sections in this package

- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/acs_commitments.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/acs-commitments)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/confirmation-response)
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
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/topology)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/traffic-control-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/versioned_google_rpc_status.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/versioned-google-rpc-status)

## Types in this section

- [com.digitalasset.canton.protocol.v30.ConfirmationResultMessage](#type-com-digitalasset-canton-protocol-v30-confirmationresultmessage)
- [com.digitalasset.canton.protocol.v30.InformeeTree](#type-com-digitalasset-canton-protocol-v30-informeetree)
- [com.digitalasset.canton.protocol.v30.MediatorReject](#type-com-digitalasset-canton-protocol-v30-mediatorreject)
- [com.digitalasset.canton.protocol.v30.ParticipantReject](#type-com-digitalasset-canton-protocol-v30-participantreject)
- [com.digitalasset.canton.protocol.v30.RejectionReason](#type-com-digitalasset-canton-protocol-v30-rejectionreason)
- [com.digitalasset.canton.protocol.v30.Verdict](#type-com-digitalasset-canton-protocol-v30-verdict)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v30-confirmationresultmessage"></a>
**Message `com.digitalasset.canton.protocol.v30.ConfirmationResultMessage`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto)
- Fields: 5

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| physical_synchronizer_id | `string` | optional |  |
| view_type | [`com.digitalasset.canton.protocol.v30.ViewType`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common#type-com-digitalasset-canton-protocol-v30-viewtype) | optional |  |
| request_id | `int64` | optional |  |
| root_hash | `bytes` | optional |  |
| verdict | [`com.digitalasset.canton.protocol.v30.Verdict`](#type-com-digitalasset-canton-protocol-v30-verdict) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-informeetree"></a>
**Message `com.digitalasset.canton.protocol.v30.InformeeTree`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| tree | [`com.digitalasset.canton.protocol.v30.GenTransactionTree`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle#type-com-digitalasset-canton-protocol-v30-gentransactiontree) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-mediatorreject"></a>
**Message `com.digitalasset.canton.protocol.v30.MediatorReject`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| reason | `google.rpc.Status` | optional |  |
| is_malformed | `bool` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-participantreject"></a>
**Message `com.digitalasset.canton.protocol.v30.ParticipantReject`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| reasons | [`com.digitalasset.canton.protocol.v30.RejectionReason`](#type-com-digitalasset-canton-protocol-v30-rejectionreason) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-rejectionreason"></a>
**Message `com.digitalasset.canton.protocol.v30.RejectionReason`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| parties | `string` | repeated |  |
| reject | [`com.digitalasset.canton.protocol.v30.LocalVerdict`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/confirmation-response#type-com-digitalasset-canton-protocol-v30-localverdict) | optional |  |
| participant_id | `string` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-verdict"></a>
**Message `com.digitalasset.canton.protocol.v30.Verdict`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| approve | `google.protobuf.Empty` | optional |  |
| participant_reject | [`com.digitalasset.canton.protocol.v30.ParticipantReject`](#type-com-digitalasset-canton-protocol-v30-participantreject) | optional |  |
| mediator_reject | [`com.digitalasset.canton.protocol.v30.MediatorReject`](#type-com-digitalasset-canton-protocol-v30-mediatorreject) | optional |  |
