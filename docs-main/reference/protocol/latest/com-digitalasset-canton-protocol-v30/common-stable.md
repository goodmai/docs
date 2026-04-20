---
title: "common_stable.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v30 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30)
- Package set: `com.digitalasset.canton.protocol.v30` | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto)

## Related sections in this package

- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/acs_commitments.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/acs-commitments)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common)
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
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/topology)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/traffic-control-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/versioned_google_rpc_status.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/versioned-google-rpc-status)

## Types in this section

- [com.digitalasset.canton.protocol.v30.AggregationRule](#type-com-digitalasset-canton-protocol-v30-aggregationrule)
- [com.digitalasset.canton.protocol.v30.GlobalKey](#type-com-digitalasset-canton-protocol-v30-globalkey)
- [com.digitalasset.canton.protocol.v30.SerializableContract](#type-com-digitalasset-canton-protocol-v30-serializablecontract)
- [com.digitalasset.canton.protocol.v30.SerializableContract.Metadata](#type-com-digitalasset-canton-protocol-v30-serializablecontract-metadata)
- [com.digitalasset.canton.protocol.v30.Stakeholders](#type-com-digitalasset-canton-protocol-v30-stakeholders)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v30-aggregationrule"></a>
**Message `com.digitalasset.canton.protocol.v30.AggregationRule`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| eligible_members | `string` | repeated |  |
| threshold | `int32` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-globalkey"></a>
**Message `com.digitalasset.canton.protocol.v30.GlobalKey`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| template_id | `bytes` | optional |  |
| key | `bytes` | optional |  |
| package_name | `string` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-serializablecontract"></a>
**Message `com.digitalasset.canton.protocol.v30.SerializableContract`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto)
- Fields: 5

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| contract_id | `string` | optional |  |
| raw_contract_instance | `bytes` | optional |  |
| metadata | [`com.digitalasset.canton.protocol.v30.SerializableContract.Metadata`](#type-com-digitalasset-canton-protocol-v30-serializablecontract-metadata) | optional |  |
| ledger_create_time | `int64` | optional |  |
| authentication_data | `bytes` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-serializablecontract-metadata"></a>
**Message `com.digitalasset.canton.protocol.v30.SerializableContract.Metadata`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| non_maintainer_signatories | `string` | repeated |  |
| non_signatory_stakeholders | `string` | repeated |  |
| key | [`com.digitalasset.canton.protocol.v30.GlobalKey`](#type-com-digitalasset-canton-protocol-v30-globalkey) | optional |  |
| maintainers | `string` | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-stakeholders"></a>
**Message `com.digitalasset.canton.protocol.v30.Stakeholders`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| all | `string` | repeated |  |
| signatories | `string` | repeated |  |
